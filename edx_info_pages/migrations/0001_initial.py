# Generated by Django 2.2.24 on 2021-09-20 14:48

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(choices=[('about', 'About'), ('contact', 'Contact'), ('faq', 'FAQ'), ('help', 'Help'), ('tos', 'TOS'), ('honor', 'Honor'), ('tos_and_honor', 'TOS and honor'), ('privacy', 'Privacy'), ('press', 'Press'), ('blog', 'Blog'), ('donate', 'Donate')], max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_rtl', models.CharField(max_length=255, null=True)),
                ('title_eo', models.CharField(max_length=255, null=True)),
                ('title_fake2', models.CharField(max_length=255, null=True)),
                ('title_am', models.CharField(max_length=255, null=True)),
                ('title_ar', models.CharField(max_length=255, null=True)),
                ('title_az', models.CharField(max_length=255, null=True)),
                ('title_bg_bg', models.CharField(max_length=255, null=True)),
                ('title_bn_bd', models.CharField(max_length=255, null=True)),
                ('title_bn_in', models.CharField(max_length=255, null=True)),
                ('title_bs', models.CharField(max_length=255, null=True)),
                ('title_ca', models.CharField(max_length=255, null=True)),
                ('title_ca@valencia', models.CharField(max_length=255, null=True)),
                ('title_cs', models.CharField(max_length=255, null=True)),
                ('title_cy', models.CharField(max_length=255, null=True)),
                ('title_da', models.CharField(max_length=255, null=True)),
                ('title_de_de', models.CharField(max_length=255, null=True)),
                ('title_el', models.CharField(max_length=255, null=True)),
                ('title_en_uk', models.CharField(max_length=255, null=True)),
                ('title_en@lolcat', models.CharField(max_length=255, null=True)),
                ('title_en@pirate', models.CharField(max_length=255, null=True)),
                ('title_es_419', models.CharField(max_length=255, null=True)),
                ('title_es_ar', models.CharField(max_length=255, null=True)),
                ('title_es_ec', models.CharField(max_length=255, null=True)),
                ('title_es_es', models.CharField(max_length=255, null=True)),
                ('title_es_mx', models.CharField(max_length=255, null=True)),
                ('title_es_pe', models.CharField(max_length=255, null=True)),
                ('title_et_ee', models.CharField(max_length=255, null=True)),
                ('title_eu_es', models.CharField(max_length=255, null=True)),
                ('title_fa', models.CharField(max_length=255, null=True)),
                ('title_fa_ir', models.CharField(max_length=255, null=True)),
                ('title_fi_fi', models.CharField(max_length=255, null=True)),
                ('title_fil', models.CharField(max_length=255, null=True)),
                ('title_fr', models.CharField(max_length=255, null=True)),
                ('title_gl', models.CharField(max_length=255, null=True)),
                ('title_gu', models.CharField(max_length=255, null=True)),
                ('title_he', models.CharField(max_length=255, null=True)),
                ('title_hi', models.CharField(max_length=255, null=True)),
                ('title_hr', models.CharField(max_length=255, null=True)),
                ('title_hu', models.CharField(max_length=255, null=True)),
                ('title_hy_am', models.CharField(max_length=255, null=True)),
                ('title_ind', models.CharField(max_length=255, null=True)),
                ('title_it_it', models.CharField(max_length=255, null=True)),
                ('title_ja_jp', models.CharField(max_length=255, null=True)),
                ('title_kk_kz', models.CharField(max_length=255, null=True)),
                ('title_km_kh', models.CharField(max_length=255, null=True)),
                ('title_kn', models.CharField(max_length=255, null=True)),
                ('title_ko_kr', models.CharField(max_length=255, null=True)),
                ('title_lt_lt', models.CharField(max_length=255, null=True)),
                ('title_ml', models.CharField(max_length=255, null=True)),
                ('title_mn', models.CharField(max_length=255, null=True)),
                ('title_mr', models.CharField(max_length=255, null=True)),
                ('title_ms', models.CharField(max_length=255, null=True)),
                ('title_nb', models.CharField(max_length=255, null=True)),
                ('title_ne', models.CharField(max_length=255, null=True)),
                ('title_nl_nl', models.CharField(max_length=255, null=True)),
                ('title_or', models.CharField(max_length=255, null=True)),
                ('title_pl', models.CharField(max_length=255, null=True)),
                ('title_pt_br', models.CharField(max_length=255, null=True)),
                ('title_pt_pt', models.CharField(max_length=255, null=True)),
                ('title_ro', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_si', models.CharField(max_length=255, null=True)),
                ('title_sk', models.CharField(max_length=255, null=True)),
                ('title_sl', models.CharField(max_length=255, null=True)),
                ('title_sq', models.CharField(max_length=255, null=True)),
                ('title_sr', models.CharField(max_length=255, null=True)),
                ('title_sv', models.CharField(max_length=255, null=True)),
                ('title_sw', models.CharField(max_length=255, null=True)),
                ('title_ta', models.CharField(max_length=255, null=True)),
                ('title_te', models.CharField(max_length=255, null=True)),
                ('title_th', models.CharField(max_length=255, null=True)),
                ('title_tr_tr', models.CharField(max_length=255, null=True)),
                ('title_uk', models.CharField(max_length=255, null=True)),
                ('title_ur', models.CharField(max_length=255, null=True)),
                ('title_vi', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_zh_cn', models.CharField(max_length=255, null=True)),
                ('title_zh_hk', models.CharField(max_length=255, null=True)),
                ('title_zh_tw', models.CharField(max_length=255, null=True)),
                ('text', tinymce.models.HTMLField()),
                ('text_en', tinymce.models.HTMLField(null=True)),
                ('text_rtl', tinymce.models.HTMLField(null=True)),
                ('text_eo', tinymce.models.HTMLField(null=True)),
                ('text_fake2', tinymce.models.HTMLField(null=True)),
                ('text_am', tinymce.models.HTMLField(null=True)),
                ('text_ar', tinymce.models.HTMLField(null=True)),
                ('text_az', tinymce.models.HTMLField(null=True)),
                ('text_bg_bg', tinymce.models.HTMLField(null=True)),
                ('text_bn_bd', tinymce.models.HTMLField(null=True)),
                ('text_bn_in', tinymce.models.HTMLField(null=True)),
                ('text_bs', tinymce.models.HTMLField(null=True)),
                ('text_ca', tinymce.models.HTMLField(null=True)),
                ('text_ca@valencia', tinymce.models.HTMLField(null=True)),
                ('text_cs', tinymce.models.HTMLField(null=True)),
                ('text_cy', tinymce.models.HTMLField(null=True)),
                ('text_da', tinymce.models.HTMLField(null=True)),
                ('text_de_de', tinymce.models.HTMLField(null=True)),
                ('text_el', tinymce.models.HTMLField(null=True)),
                ('text_en_uk', tinymce.models.HTMLField(null=True)),
                ('text_en@lolcat', tinymce.models.HTMLField(null=True)),
                ('text_en@pirate', tinymce.models.HTMLField(null=True)),
                ('text_es_419', tinymce.models.HTMLField(null=True)),
                ('text_es_ar', tinymce.models.HTMLField(null=True)),
                ('text_es_ec', tinymce.models.HTMLField(null=True)),
                ('text_es_es', tinymce.models.HTMLField(null=True)),
                ('text_es_mx', tinymce.models.HTMLField(null=True)),
                ('text_es_pe', tinymce.models.HTMLField(null=True)),
                ('text_et_ee', tinymce.models.HTMLField(null=True)),
                ('text_eu_es', tinymce.models.HTMLField(null=True)),
                ('text_fa', tinymce.models.HTMLField(null=True)),
                ('text_fa_ir', tinymce.models.HTMLField(null=True)),
                ('text_fi_fi', tinymce.models.HTMLField(null=True)),
                ('text_fil', tinymce.models.HTMLField(null=True)),
                ('text_fr', tinymce.models.HTMLField(null=True)),
                ('text_gl', tinymce.models.HTMLField(null=True)),
                ('text_gu', tinymce.models.HTMLField(null=True)),
                ('text_he', tinymce.models.HTMLField(null=True)),
                ('text_hi', tinymce.models.HTMLField(null=True)),
                ('text_hr', tinymce.models.HTMLField(null=True)),
                ('text_hu', tinymce.models.HTMLField(null=True)),
                ('text_hy_am', tinymce.models.HTMLField(null=True)),
                ('text_ind', tinymce.models.HTMLField(null=True)),
                ('text_it_it', tinymce.models.HTMLField(null=True)),
                ('text_ja_jp', tinymce.models.HTMLField(null=True)),
                ('text_kk_kz', tinymce.models.HTMLField(null=True)),
                ('text_km_kh', tinymce.models.HTMLField(null=True)),
                ('text_kn', tinymce.models.HTMLField(null=True)),
                ('text_ko_kr', tinymce.models.HTMLField(null=True)),
                ('text_lt_lt', tinymce.models.HTMLField(null=True)),
                ('text_ml', tinymce.models.HTMLField(null=True)),
                ('text_mn', tinymce.models.HTMLField(null=True)),
                ('text_mr', tinymce.models.HTMLField(null=True)),
                ('text_ms', tinymce.models.HTMLField(null=True)),
                ('text_nb', tinymce.models.HTMLField(null=True)),
                ('text_ne', tinymce.models.HTMLField(null=True)),
                ('text_nl_nl', tinymce.models.HTMLField(null=True)),
                ('text_or', tinymce.models.HTMLField(null=True)),
                ('text_pl', tinymce.models.HTMLField(null=True)),
                ('text_pt_br', tinymce.models.HTMLField(null=True)),
                ('text_pt_pt', tinymce.models.HTMLField(null=True)),
                ('text_ro', tinymce.models.HTMLField(null=True)),
                ('text_ru', tinymce.models.HTMLField(null=True)),
                ('text_si', tinymce.models.HTMLField(null=True)),
                ('text_sk', tinymce.models.HTMLField(null=True)),
                ('text_sl', tinymce.models.HTMLField(null=True)),
                ('text_sq', tinymce.models.HTMLField(null=True)),
                ('text_sr', tinymce.models.HTMLField(null=True)),
                ('text_sv', tinymce.models.HTMLField(null=True)),
                ('text_sw', tinymce.models.HTMLField(null=True)),
                ('text_ta', tinymce.models.HTMLField(null=True)),
                ('text_te', tinymce.models.HTMLField(null=True)),
                ('text_th', tinymce.models.HTMLField(null=True)),
                ('text_tr_tr', tinymce.models.HTMLField(null=True)),
                ('text_uk', tinymce.models.HTMLField(null=True)),
                ('text_ur', tinymce.models.HTMLField(null=True)),
                ('text_vi', tinymce.models.HTMLField(null=True)),
                ('text_uz', tinymce.models.HTMLField(null=True)),
                ('text_zh_cn', tinymce.models.HTMLField(null=True)),
                ('text_zh_hk', tinymce.models.HTMLField(null=True)),
                ('text_zh_tw', tinymce.models.HTMLField(null=True)),
                ('site', models.ForeignKey(default=1, help_text='The Site that this provider configuration belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='info_pages', to='sites.Site')),
            ],
            options={
                'unique_together': {('page', 'site')},
            },
        ),
    ]