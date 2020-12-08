Add to your `httpd.conf`:

```
<Directory "<your path>/zadanie_8">
    Options Indexes FollowSymLinks Includes ExecCGI
    AllowOverride All
    Require all granted
</Directory>
```