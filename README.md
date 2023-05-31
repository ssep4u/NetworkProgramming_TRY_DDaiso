# DDaiso
- **프로젝트이름/urls.py -> 앱이름/urls.py -> 앱이름/views.py -> 앱이름/models.py -> templates/앱이름/HTML파일이름.html**
- admin.py: 관리자 사이트
- form.py: 입력폼 사이트
- 개발 순서: models.py, views.py, urls.py, templates
---
1. startproject
   1. python -m pip install django~=3.2
   2. django-admin startproject DDaiso .
   3. python manage.py runserver
   4. Enable Django Support
   5. git 설정
2. startapp product
   1. python manage.py startapp product
   2. 'product', in INSTALLED_APPS in settings.py
3. product/
   1. models
      1. Product
         1. name
         2. price
         3. python manage.py makemigrations product
            - models -> DB로 옮기기 위한 py 만들기
         4. python manage.py migrate product
            - DB 테이블 만들기
         5. \_\_str\_\_()
         6. get_absolute_url()
   2. shell_plus
      1. python -m pip install django-extensions
      2. 'django_extensions', in INSTALLED_APPS in settings.py
         - -(빼기) 아니라 _(밑줄)
      3. python manage.py shell_plus
   3. admin
      1. Product
      2. python manage.py createsuperuser
   4. R: ProductListView
      1. views
         1. ProductListView
      2. urls
         1. product:list
      3. templates/product/
         1. product_list.html <- product_list
   5. R: ProductDetailView
      1. views
         1. ProductDetailView
      2. urls
         1. product:detail
      3. templates/product/
         1. product_detail.html
            1. add Go to Product List link
         2. add detail link in product_list.html
            ```html
            <a href="{% url 'product:detail' pk=product.id %}">{{ product.name }}</a>
            ```
   6. C: ProductCreateView
      1. views
         1. ProductCreateView
      2. urls
         1. product:add
      3. templates/product/
         1. product_create.html
            ```html
            <form action="" method="post">
                {% csrf_token %}
                {{ form.as_p }}
                <input type="submit" value="Add">
            </form>
            ```
         2. **Add Product** in product_list.html
            ```html
            <a href="{% url 'product:add' %}">Add Product</a>
            ```
   7. U: ProductUpdateView
      1. views
         1. ProductUpdateView
      2. urls
         1. product:edit
      3. templates/product/
         1. product_update.html
         2. add **EDIT** link in product_list.html
   8. D: ProductDeleteView
      1. views
         1. ProductDeleteView
      2. urls
         1. product:remove
      3. templates/product/
         1. product_confirm_delete.html
         2. add **REMOVE** link in product_list.html
   9. 🧨🎉✨기능 완성
4. DDaiso/urls
   1. / -> product:list
---
## feature/cloudtype
1. local
   1. pip freeze > requirements.txt
   2. ALLOWED_HOSTS = ['*'] in settings.py
2. cloudtype
   1. python manage.py makemigrations
   2. python manage.py migrate
---
## feature/bootstrap
1. html 내용 중 중복된 것 합치고, 실제 바뀌어야 하는 부분만 남기자
   1. extends 'base.html'; block title, content
   2. add DIRS in TEMPLATES in settings.py
2. add Bootstrap css, js file
   1. static/css/bootstrap.min.css, static/js/bootstrap.min.js
   2. add STATIC_ROOT, STATICFILES_DIRS in settings.py
   3. add Bootstrap class in .html
   4. pagination
---
## feature/FBV
1. FBV list_product
   1. product/views
   2. product/urls
   3. DDaiso/urls
2. FBV detail_product
   1. product/views
   2. product/urls
   3. product/templates/product/product_list, product_detail.html
3. FBV create_product
   1. product/forms
   2. product/views
   3. product/urls
   4. product/templates/product/product_list
4. FBV update_product
   1. product/forms 
   2. product/views
   3. product/urls
   4. product/templates/product/product_list