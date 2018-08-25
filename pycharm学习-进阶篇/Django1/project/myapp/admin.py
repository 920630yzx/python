from django.contrib import admin

# Register your models here.
from .models import Grades,Students

class StudentsInfo(admin.TabularInline):  # StackedInline
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    # 列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']  # 定义列表的列名,'pk'不能自己设置
    list_filter = ['gname']  # 定义过滤器,起到挑选的作用,这里表示按照gname列来挑选
    search_fields = ['gname']  # 定义搜索器,这里表示按照gname来搜索
    list_per_page = 5   # 添加页,这里表示5行显示成1页
    # 添加、修改页属性
    # fields = ['ggirlnum','gboynum','gname','gdate','isDelete']  # fields规定属性的先后顺序
    fieldsets = [   # fieldsets给属性进行分租,且fields和fieldsets不能同时使用
        ("num",{"fields":['ggirlnum','gboynum']}),
        ("base",{"fields":['gname','gdate','isDelete']}),  # 这里分成了两组
    ]

class StudentsAdmin(admin.ModelAdmin):
    def gender(self):  # 修改男女的标签,将其改为性别'男','女';之后再修改下面的列表名即可
        if self.sgeder:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'   # 设置页面gender列的名称,对其进行描述
    list_display = ['pk', 'sname', 'sage', gender, 'scontend', 'sgrade', 'isDelete']  # 定义列表的列名
    actions_on_top = False  # 设置执行动作的位置,删除顶部
    actions_on_bottom = True   # 执行动作的位置,添加底部

# 注册
# admin.site.register(Grades)
admin.site.register(Grades, GradesAdmin)
admin.site.register(Students, StudentsAdmin)   # 也可以用装饰器注册,方法：在class StudentsAdmin(admin.ModelAdmin)前加上@admin.register(Students)；将这行注释掉