from django.contrib import admin
from models import Company,CompetenceTeam, TeamMember, Skill, Skill_user,Skill_CT

# Register your models here.
admin.site.register(Company,admin.ModelAdmin)
admin.site.register(CompetenceTeam,admin.ModelAdmin)
admin.site.register(TeamMember,admin.ModelAdmin)
admin.site.register(Skill,admin.ModelAdmin)
admin.site.register(Skill_user,admin.ModelAdmin)
admin.site.register(Skill_CT,admin.ModelAdmin)
