from rest_framework import viewsets
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
import threading
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# Create your views here.
from rest_framework.response import Response

class AssetsViewSet(viewsets.ViewSet):

    def create(self, request):
        data = request.data
        serializer = AssetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request,pk=None):
        if pk:
            queryset=Assets.objects.filter(id=pk)
        else:
            queryset=Assets.objects.all()
        serializer = AssetsSerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request,pk=None):
        try:
            queryset=Assets.objects.get(id=pk)
            if queryset:
                queryset.delete()
        
            return Response({"message": "Assets deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Assets.DoesNotExist:
            return Response({"message": "Assets not found."}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            asset = Assets.objects.get(pk=pk) 
        except Assets.DoesNotExist:
            return Response({"message": "Asset not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AssetsSerializer(asset, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class Assetpdf(APIView):

    def generate_pdf_report(self,pk):
        assets = Assets.objects.filter(id=int(pk))
        file_path = f"media/reports/asset_report_{pk}.pdf"
        c = canvas.Canvas(file_path, pagesize=letter)
        y = 750
        c.drawString(100, y, "ID | Name | Category | Purchase Date")
        y -= 20
        for asset in assets:
            c.drawString(100, y, f"{asset.id} | {asset.name} | {asset.category} | {asset.purchase_date}")
            y -= 20
        c.save()
        return file_path

    def generate_pdf_background(self,pk):
        thread = threading.Thread(target=self.generate_pdf_report,args=(pk))
        thread.start()

    def get(self,request):
        pk= request.GET.get('id')
        self.generate_pdf_background(pk)
        return Response({"message": "Report generation started. PDF will be saved soon."},status=status.HTTP_200_OK)
