"""
Alert management module.

Creates and manages SOC alerts.
"""

from datetime import datetime
import uuid


class AlertManager:
    """
    Handles security alert creation.
    """


    def create_alert(
        self,
        incident,
        risk
    ):
        """
        Generate structured alert.
        """

        alert = {

            "alert_id":
                f"ALERT-{uuid.uuid4().hex[:8].upper()}",


            "timestamp":
                datetime.utcnow().isoformat(),


            "title":
                incident.get("incident"),


            "severity":
                incident.get("severity"),


            "risk_score":
                risk.get("score"),


            "risk_level":
                risk.get("risk"),


            "description":
                incident.get("description"),


            "mitre":
                incident.get("mitre"),


            "status":
                "NEW"
        }


        return alert
