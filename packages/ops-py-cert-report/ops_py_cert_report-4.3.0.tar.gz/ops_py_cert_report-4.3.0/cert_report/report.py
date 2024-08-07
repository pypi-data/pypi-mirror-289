#!/usr/bin/env python

from operator import itemgetter

########################################################################################################################


def get_html_table(header, rows):
    """generates and returns a html table bases on the provided header and html rows (<tr>)"""

    html_table = f"""<table bordercolor='black' border='2'>
    <thead>
    <tr style='background-color: Teal; color: White'>
"""
    for h in header:
        html_table += f"""        <th>{h}</th>
"""

    html_table += f"""    </tr>
    </thead>
    <tbody>
{rows}    </tbody>
</table>
"""
    return html_table


class Report(object):
    """A psycopg class to connect to a PostgreSQL database and execute queries

        Attributes
        ----------

        certs : the list of ssl certs (dict objects) to generate report for
        warning : the expiry in days threshold to mark the ssl with a WARNING
        critical : the expiry in days threshold to mark the ssl as CRITICAL
        ok_symbol : Slack emoji OK symbol
        warning_symbol : Slack emoji WARNING symbol
        critical_symbol : Slack emoji CRITICAL symbol
        error_symbol : Slack emoji ERROR symbol
        expired_symbol : Slack emoji EXPIRED symbol
        unknown_symbol : Slack emoji UNKNOWN symbol
        ok_txt = OK status text (green html background)
        warning_txt = WARNING status text (yellow html background)
        critical_txt = CRITICAL status text (red html background)
        error_txt = ERROR status text (purple html background)
        expired_txt = EXPIRED status text (red html background)
        unknown_txt = UNKNOWN status text (yellow html background)
        alert_styles : dict with key / value pairs of status texts and html td tags with color background
        ok_code : 0
        warning_code : 1
        critical_code : 2
        error_code : 3
        expired_code : 4
        unknown_code : 5
        title : The title of the report
        html_header : The html table column names
        skip_ok : If SSL certs with no warning or other errors will be included in the report (as OK green)
        report_json : the list of each ssl cert report as json
        self.html_rows : the list of each ssl cert report as html row
        self.slack_rows : the list of each ssl cert report as slack markdown row

        Methods
        -------

        get_html_row(row)
            Parses through each element in the passed list (row) and create a html <tr> row.
            Applies background color based on status code in the provided list.
        gen_report()
            Parses through the list of provided ssl certs. Creates a dict for each ssl cert with,
            - the name of each cert
            - expire date
            - expire age in days
            - comment
            - status
            - status code

           Lists to be used for Slack Markdown row are created and added to a list of Slack Rows
           and list of HTML row are created, to generate html row, and then added to html table rows.
           A dict report of each ssl cert check is added to a json report list

        get_slack_report()
            Sorts and return the Slack report.
        get_html_report()
            Sorts the html rows, call the get_html_table function and returns the html table as result.
        get_report_json()
            Returns the list of ssl certs dict reports
    """

    def __init__(self, certs, warning, critical,
                 ok_symbol=":white_check_mark:",
                 warning_symbol=":warning:",
                 critical_symbol=":bangbang:",
                 error_symbol=":no_entry:",
                 expired_symbol=":rotating_light:",
                 unknown_symbol=":question:",
                 ok_txt="OK",
                 warning_txt="Warning",
                 critical_txt="Critical!!",
                 error_txt="Error",
                 expired_txt="Expired!!",
                 unknown_txt="Unknown",
                 title="SSL certificates report",
                 html_header=None,
                 skip_ok=False):

        if html_header is None:
            html_header = ["Status", "SSL Cert", "Message", "Expiration date"]

        green = "<td style='background-color: Green; color: White; font-weight:bold'>"
        purple = "<td style='background-color: Purple; color: White; font-weight:bold'>"
        yellow = "<td style='background-color: Yellow; color: Black; font-weight:bold'>"
        red = "<td style='background-color: Red; color: White; font-weight:bold'>"

        self.certs = certs
        self.warning = warning
        self.critical = critical

        self.ok_symbol = ok_symbol
        self.warning_symbol = warning_symbol
        self.critical_symbol = critical_symbol
        self.error_symbol = error_symbol
        self.expired_symbol = expired_symbol
        self.unknown_symbol = unknown_symbol

        self.ok_txt = ok_txt
        self.warning_txt = warning_txt
        self.critical_txt = critical_txt
        self.error_txt = error_txt
        self.expired_txt = expired_txt
        self.unknown_txt = unknown_txt

        self.alert_styles = {
            self.ok_txt: green,
            self.error_txt: purple,
            self.warning_txt: yellow,
            self.unknown_txt: yellow,
            self.critical_txt: red,
            self.expired_txt: red
        }

        self.ok_code = 0
        self.warning_code = 1
        self.critical_code = 2
        self.error_code = 3
        self.expired_code = 4
        self.unknown_code = 5

        self.title = title
        self.html_header = html_header
        self.skip_ok = skip_ok

        self.report_json = []
        self.html_rows = []
        self.slack_rows = []

    def get_html_row(self, row):
        """parses through the passed list and creates a html row with background color based on the status codes"""

        html_row = f"    <tr>"
        for item in row:
            td = self.alert_styles.get(item, '<td>')
            html_row += f"""
            {td}{item}</td>"""
        html_row += """
        </tr>"""
        if row:
            return html_row

    def gen_report(self):
        """parses through the list of provided ssl certs to generate html, slack and json reports"""

        for c in self.certs:
            name = c.get("name")
            expire_date = c.get("notAfter")
            days = c.get("expire_age")
            error_message = c.get("error_message")
            crt = {"name": name,
                   "expire_date": expire_date,
                   "expire_age": days,
                   "comment": error_message,
                   "status": self.unknown_txt,
                   "code": self.unknown_code
                   }

            # add error message if any
            if error_message:
                # strip this kind of unnecessary long error message
                error = "certificate is not valid"
                if error in error_message:
                    error_message = f"{error_message.split(error)[0]}{error}"

                expire_date = "-"
                slack_row = f"{self.error_symbol} *{name}* - {error_message}"
                html_row = [self.error_txt, name, error_message, expire_date]
                crt["status"] = self.error_txt
                crt["code"] = self.error_code

            # if not error message, then check the expiration date and add comment, code and status accordingly
            elif not error_message and isinstance(days, int) and days < 0:
                comment = f"Will expire in {abs(days)} days"
                slack_row = f"*{name}* - {comment} ({expire_date})."
                html_row = [name, comment, expire_date]
                crt["comment"] = comment

                if abs(days) <= self.critical:
                    slack_row = f"{self.critical_symbol} {slack_row}"
                    html_row = [self.critical_txt] + html_row
                    crt["status"] = self.critical_txt
                    crt["code"] = self.critical_code
                elif self.warning >= abs(days) > self.critical:
                    slack_row = f"{self.warning_symbol} {slack_row}"
                    html_row = [self.warning_txt] + html_row
                    crt["status"] = self.warning_txt
                    crt["code"] = self.warning_code
                else:
                    crt["status"] = self.ok_txt
                    crt["code"] = self.ok_code
                    html_row = [self.ok_txt] + html_row
                    slack_row = f"{self.ok_symbol} {slack_row}"
                    if self.skip_ok:
                        html_row = []
                        slack_row = []

            # if not error message, but the cert has already expired
            elif not error_message and isinstance(days, int) and days >= 0:
                comment = f"Has already expired. Expired {abs(days)} days ago."
                slack_row = f"{self.expired_symbol} *{name}* - {comment} ({expire_date})."
                html_row = [self.expired_txt, name, comment, expire_date]
                crt["comment"] = comment
                crt["status"] = self.critical_txt
                crt["code"] = self.critical_code
            else:
                comment = f"Unknown state for cert **{name}**."
                slack_row = f"{self.unknown_symbol} - *{name}* - {comment} ({expire_date})."
                html_row = [self.unknown_txt, name, comment, "-"]
                crt["comment"] = comment
                crt["status"] = self.unknown_txt
                crt["code"] = self.unknown_code

            # get the code to be used for the html row and slack row
            code = crt.get("code")

            if html_row:
                html_syntax = self.get_html_row(html_row)
                self.html_rows.append([code, days, html_syntax])

            if slack_row:
                self.slack_rows.append([code, days, slack_row])

            self.report_json.append(crt)

    def get_slack_report(self):
        """sorts and return the Slack Markdown report"""

        rows = ""
        for row in sorted(self.slack_rows, key=itemgetter(0, 1, 2), reverse=True):
            rows += f"{row[-1]}\n"

        if rows:
            return f"*{self.title}*\n{rows}"

    def get_html_report(self):
        """sorts the html rows, call the get_html_table function and then returns the html table as a result"""

        rows = ""
        for row in sorted(self.html_rows, key=itemgetter(0, 1, 2), reverse=True):
            rows += f"{row[-1]}\n"

        if rows:
            return self.title, get_html_table(self.html_header, rows)

        return None, None

    def get_report_json(self):
        """returns the list of ssl certs dict reports"""

        return self.report_json
