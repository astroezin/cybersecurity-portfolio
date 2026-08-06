
"""
Risk scoring engine.

Calculates security risk based on
events and incidents.
"""


class RiskScorer:
    """
    Assigns risk scores.
    """


    SEVERITY_POINTS = {

        "LOW": 10,

        "MEDIUM": 30,

        "HIGH": 60,

        "CRITICAL": 90

    }


    def calculate_score(self, severity):
        """
        Convert severity into score.
        """

        return self.SEVERITY_POINTS.get(
            severity.upper(),
            0
        )


    def calculate_risk_level(self, score):
        """
        Convert score into risk level.
        """

        if score >= 80:
            return "CRITICAL"

        elif score >= 50:
            return "HIGH"

        elif score >= 25:
            return "MEDIUM"

        elif score > 0:
            return "LOW"

        else:
            return "INFORMATIONAL"



    def analyze(self, incident):
        """
        Analyze incident risk.
        """

        score = self.calculate_score(
            incident.get("severity")
        )

        return {

            "score": score,

            "risk":
                self.calculate_risk_level(score)

        }
