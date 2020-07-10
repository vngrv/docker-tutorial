from django.urls import path
from dances.views import *

urlpatterns = [
    # path('part/', Part.as_view()),
    path('wsh_all/', Wsh.as_view()),
    path('user_info/', UserInfo.as_view()),
    # path('not_incl/', NotInclPeople.as_view()),
    # path('remove_part/', RemovePartic.as_view()),
    path('add_wsh/', CreateWSH.as_view()),
    path('halls_for_school/', HallsForSchool.as_view()),
    path('all_schools/', AllSchools.as_view()),
    path('all_styles/', AllStyles.as_view()),
    path('teachers_for_style/', TeachersForStyle.as_view()),
    path('add_teachers_for_wsh/', AddTeachersForWSH.as_view()),
    path('query_for_part/', AskForPart.as_view()),
    path('query_part_info/', QueryPartInfo.as_view()),
    path('profile_upd/<int:pk>/', UpdateProfile.as_view({'post':'update'})),
    path('write_feedback/', WriteFeedback.as_view()),
    path('teachers/', AllTeachers.as_view()),
    path('one_teacher/', TeacherInfo.as_view()),
    path('feedbacks/', FeedbackForTeacher.as_view()),
    path('participants/', PartcipantsPerWSH.as_view()),
    # path('quieries_to_approve/', AllQueryPartInfo.as_view()),
    path('quieries_to_approve2/', AllQueryPartInfo2.as_view()),
    path('approve_query/', ApprovePartQueryAndAddPart.as_view()),
    path('profile_new/', AddNameForNewProfile.as_view()),
    path('report/', ProfitInfo.as_view()),
    # path('all_teachers/', AllTeachers.as_view()),
    # path('wsh_nearest/', NearestWshForTeacher.as_view()),
    path('wsh_filter/', FilteredWSH.as_view()),
    path('rating/', RatingUsers.as_view()),
    # path('wsh_upd/<int:pk>/', UpdateWSH.as_view({'post':'update'})),
    # path('one_part/', OnePart.as_view()),
    # path('style_check/', DanceStyleGen.as_view()),
]