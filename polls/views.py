from django.utils import timezone
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    """
    IndexView displays a list of the latest published questions.

    Attributes:
        template_name (str): The name of the template to use for rendering the view.
        context_object_name (str): The name of the context variable to use in the template.
    """

    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Returns the last five published questions.

        Filters the questions to include only those with a publication date less than or equal to the current time,
        and orders them by publication date in descending order.

        Returns:
            QuerySet: A queryset containing the last five published questions.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    """
    DetailView displays the details of a specific question.

    Attributes:
        model (Model): The model to use for the view.
        template_name (str): The name of the template to use for rendering the view.
    """

    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.

        Filters the questions to include only those with a publication date less than or equal to the current time.

        Returns:
            QuerySet: A queryset containing the published questions.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """
    ResultsView displays the results of a specific question.

    Attributes:
        model (Model): The model to use for the view.
        template_name (str): The name of the template to use for rendering the view.
    """

    model = Question
    template_name = "polls/results.html"


class VoteView(generic.View):
    """
    VoteView handles the voting process for a specific question.

    This class is a placeholder for the voting logic, which should be implemented in the future.
    """

    pass
