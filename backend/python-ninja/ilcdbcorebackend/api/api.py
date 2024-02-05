
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from api.models import OJT_Trainies
from api.schemas import OJT_TrainiesSchema, OJT_TrainiesCreateSchema

app = NinjaAPI()

# get all ojt trainies
@app.get("ojttrainies/", response=list[OJT_TrainiesSchema])
def get_ojttrainies(request):
    return OJT_Trainies.objects.all()


# get single ojt trainy
@app.get("ojttrainies/{id}/", response=OJT_TrainiesSchema)
def get_ojttrainy(request, id: int):
    ojt = get_object_or_404(OJT_Trainies, id = id)
    return ojt


@app.post("ojttrainies/", response=OJT_TrainiesSchema)
def create_ojt(request, ojt: OJT_TrainiesCreateSchema):
    ojt_data = ojt.model_dump()
    ojt_model = OJT_Trainies.objects.create(**ojt_data)
    return ojt_model



















