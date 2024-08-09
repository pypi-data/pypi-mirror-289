import csv
import datetime as dt

from pretalx.event.models import Event
from pretalx.person.models import SpeakerProfile, User
from pretalx.submission.models import Answer, Question, Submission


def import_wtd_submissions():
    event = Event.objects.get(slug="wtd-portland-2020")
    question_mapping = {
        "who_and_why": 254,  # submission
        "other_information": 255,  # submission
        "twitter_handle": 257,  # speaker
        "personal_website": 277,  # speaker
        "code_of_conduct": 256,  # submission
    }
    for key, value in question_mapping.items():
        question_mapping[key] = Question.objects.get(event=event, pk=value)
    known_speakers = {}
    mail_text = """Hey Folks,

Write the Docs is using Pretalx to process talk proposals this year, and we've imported your proposal(s) from https://docs.google.com/forms/d/1Kpi_wugQC8xF1QiLbfr0Ii5xdJWf97xyGbY7lxCKTME/.

We've automatically created an account for you, using the date from the Form. You can reset your password using this link, and update things like your website, twitter account or headshot:

    {url}

We'll let you know whether your proposal has been accepted by the end of the month, the 30th to be precise.

Any questions just drop me a line at portland@writethedocs.org

Cheers
Sam"""

    with open("Write the Docs Portland 2020 Call for Proposals.csv") as import_file:
        reader = csv.DictReader(import_file)
        all_data = list(reader)

    new_users = []
    for data in all_data:
        email = data["Username"].lower().strip()
        if email in known_speakers:
            speaker = known_speakers[email]
        else:
            speaker, created = User.objects.get_or_create(email=email)
            if created:
                new_users.append(speaker)
        known_speakers[email] = speaker
        speaker.name = data["Name"]
        speaker.save()

        SpeakerProfile.objects.get_or_create(user=speaker, event=event)

        twitter_answer, _ = Answer.objects.get_or_create(
            person=speaker, question=question_mapping["twitter_handle"]
        )
        twitter_answer.answer = data["Twitter Handle"]
        twitter_answer.save()

        website_answer, _ = Answer.objects.get_or_create(
            person=speaker, question=question_mapping["personal_website"]
        )
        website_answer.answer = data["Personal Website "]
        website_answer.save()

        submission, _ = Submission.objects.get_or_create(
            event=event,
            title=data["Talk Title"],
            defaults={"submission_type": event.cfp.default_type},
        )
        submission.speakers.set([speaker])
        submission.abstract = data["Talk Abstract"]
        submission.save()

        who_answer, _ = Answer.objects.get_or_create(
            submission=submission, question=question_mapping["who_and_why"]
        )
        who_answer.answer = data["Who and Why"]
        who_answer.save()

        other_answer, _ = Answer.objects.get_or_create(
            submission=submission, question=question_mapping["other_information"]
        )
        other_answer.answer = data["Other Information"]
        other_answer.save()

        coc_answer, _ = Answer.objects.get_or_create(
            submission=submission, question=question_mapping["code_of_conduct"]
        )
        coc_answer.answer = "True"
        coc_answer.save()

        Submission.objects.filter(code=submission.code).update(
            created=dt.datetime.strptime(
                data["Timestamp"], "%Y/%m/%d %H:%M:%S %p GMT+1"
            )
        )

    for user in new_users:
        user.reset_password(event=event, mail_text=mail_text, orga=False)
