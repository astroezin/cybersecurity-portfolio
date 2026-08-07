"""
SIEM Alert Dashboard

Main Flask application.
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import abort

from core.loader import load_alerts
from core.statistics import calculate_statistics
from core.logger import setup_logger


logger = setup_logger()

app = Flask(__name__)


@app.route("/")
def dashboard():
    """
    Dashboard page.
    """

    alerts = load_alerts()

    severity = request.args.get(
        "severity"
    )

    status = request.args.get(
        "status"
    )

    search = request.args.get(
        "search"
    )

    if severity:

        alerts = [

            alert

            for alert in alerts

            if alert.get(
                "severity",
                ""
            ).lower() == severity.lower()

        ]

    if status:

        alerts = [

            alert

            for alert in alerts

            if alert.get(
                "status",
                ""
            ).lower() == status.lower()

        ]

    if search:

        keyword = search.lower()

        alerts = [

            alert

            for alert in alerts

            if (

                keyword in alert.get(
                    "title",
                    ""
                ).lower()

                or

                keyword in alert.get(
                    "username",
                    ""
                ).lower()

                or

                keyword in alert.get(
                    "source_ip",
                    ""
                ).lower()

                or

                keyword in alert.get(
                    "alert_id",
                    ""
                ).lower()

            )

        ]

    stats = calculate_statistics(
        alerts
    )

    logger.info(
        "Dashboard viewed"
    )

    return render_template(

        "index.html",

        alerts=alerts,

        stats=stats

    )


@app.route("/alert/<alert_id>")
def alert_details(
    alert_id
):
    """
    Alert details page.
    """

    alerts = load_alerts()

    for alert in alerts:

        if alert.get(
            "alert_id"
        ) == alert_id:

            logger.info(
                f"Opened alert {alert_id}"
            )

            return render_template(

                "alert.html",

                alert=alert

            )

    abort(
        404
    )


@app.route("/reports")
def reports():
    """
    Reports page.
    """

    alerts = load_alerts()

    stats = calculate_statistics(
        alerts
    )

    return render_template(

        "reports.html",

        alerts=alerts,

        stats=stats

    )


@app.errorhandler(404)
def page_not_found(error):
    """
    Custom 404 page.
    """

    return (

        "<h2>404 - Page Not Found</h2>",

        404

    )


@app.errorhandler(500)
def server_error(error):
    """
    Custom 500 page.
    """

    logger.exception(
        "Internal Server Error"
    )

    return (

        "<h2>500 - Internal Server Error</h2>",

        500

    )


if __name__ == "__main__":

    logger.info(
        "Starting SIEM Alert Dashboard"
    )

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
