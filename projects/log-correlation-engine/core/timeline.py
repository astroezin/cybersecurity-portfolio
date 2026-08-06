"""
Incident timeline generator.

Builds chronological security events.
"""

from datetime import datetime


class TimelineBuilder:
    """
    Creates attack timelines.
    """


    def __init__(self):
        self.events = []


    def add_event(self, event):
        """
        Add event to timeline.
        """

        self.events.append(event)



    def generate(self):
        """
        Generate ordered timeline.
        """

        timeline = []


        for index, event in enumerate(
            self.events,
            start=1
        ):

            timeline.append(
                {
                    "step": index,

                    "event":
                        event.get(
                            "event_type"
                        ),

                    "user":
                        event.get(
                            "username"
                        ),

                    "source_ip":
                        event.get(
                            "source_ip"
                        )
                }
            )


        return timeline
