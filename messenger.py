from fbmq import QuickReply, Template
from example.fbpage import page

USER_SEQ = {}

@page.handle_message
def received_message(event):
    sender_id = event.sender_id
    message = event.message

    if not message:
        page.send(sender_id, "🚫 عذرًا، لم يتم استلام أي رسالة صالحة.")
        return

    message_text = message.get("text")
    
    # التعامل مع الرسائل المدخلة من المستخدم
    if message_text == "السلام عليكم":
        page.send(sender_id, "عليكم السلام 😊") 
    elif message_text == "📚 أسعار الكورسات":
        show_course_prices(sender_id)
    elif message_text == "💡 سعر الاشراف":
        show_supervision_prices(sender_id)
    elif message_text == "✅ هل المنصة معتمدة؟":
        show_platform_approval(sender_id)
    elif message_text == "📝 كيفية التسجيل؟":
        show_registration_info(sender_id)
    elif message_text == "💬 تواصل مع الدعم":
        show_support_options(sender_id)
    elif message_text == "🚀 أريد الانضمام":
        show_join_info(sender_id)
else:
    page.send(sender_id, "مرحبًا! اختر من الخيارات التالية:", quick_replies=[
        QuickReply(title="📚 أسعار الكورسات", payload=f"COURSES_PRICE_{sender_id}"),
        QuickReply(title="💡 سعر الاشراف", payload=f"SUPERVISION_PRICE_{sender_id}"),
        QuickReply(title="✅ هل المنصة معتمدة؟", payload=f"PLATFORM_APPROVAL_{sender_id}"),
        QuickReply(title="📝 كيفية التسجيل؟", payload=f"REGISTRATION_{sender_id}"),
        QuickReply(title="💬 تواصل مع الدعم", payload=f"SUPPORT_{sender_id}"),
        QuickReply(title="🚀 أريد الانضمام", payload=f"JOIN_{sender_id}")
    ])
    print(f"تم إرسال الرد للمستخدم: {sender_id}")  # استخدم هذا السطر للتحقق من الإرسال

    # تحديث حالة الرسالة
    USER_SEQ[sender_id] = message_text  # تحديث مع سجل الرسائل





def show_course_prices(sender_id):
    USER_SEQ[sender_id] = "COURSES_PRICE"
    page.send(sender_id, Template.Generic([ 
        Template.GenericElement("كورس ABAT - فني تحليل سلوك تطبيقي", 
                                subtitle="كورس فني معتمد لتعليم تحليل السلوك التطبيقي باستخدام تقنيات علمية متطورة لتقييم وتعديل السلوك 💡", 
                                image_url="https://github.com/user-attachments/assets/5a42a654-144e-4ea0-a44f-d6f58ae95c73", 
                                buttons=[Template.ButtonWeb("🌐 سجل الأن", "https://www.highnessc.com/abat-aba/"),
                                         Template.ButtonPostBack("السعر 💰5000 ج", "PRICE_ABAT")]), 
        Template.GenericElement("كورس QASP-S - مشرف توحد مؤهل", 
                                subtitle="كورس معتمد لتأهيل مشرفي التوحد لقيادة فرق العمل وتقديم الدعم للأفراد ذوي التوحد 🎯", 
                                image_url="https://github-production-user-asset-6210df.s3.amazonaws.com/135191663/388782998-a46138cd-feac-40a1-8eda-34851b566f51.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241122%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241122T025945Z&X-Amz-Expires=300&X-Amz-Signature=bb0099d5e0615be7aefd194dacf61afafcaa945e4d3140e8b545efbb81fd78fa&X-Amz-SignedHeaders=host", 
                                buttons=[Template.ButtonWeb("🌐 سجل الأن", "https://www.highnessc.com/qasps-aba/"),
                                         Template.ButtonPostBack("السعر 💰15000 ج", "PRICE_QASP-S")]), 
        Template.GenericElement("كورس QBA - محلل سلوك مؤهل", 
                                subtitle="كورس متخصص لتأهيل محللي السلوك باستخدام أحدث الأساليب العلمية لتحليل السلوك وتقديم التدخلات السلوكية 🧠", 
                                image_url="https://github.com/user-attachments/assets/50ead23c-e000-4f5a-b5be-23a24887f517", 
                                buttons=[Template.ButtonWeb("🌐 سجل الأن", "https://www.highnessc.com/qba-certification/"),
                                         Template.ButtonPostBack("السعر 💰25000 ج", "PRICE_QBA")])
    ]))
    show_main_menu(sender_id)




def show_supervision_prices(sender_id):
    """
    عرض أسعار الإشراف المتاحة للمستخدم.
    """
    USER_SEQ[sender_id] = "SUPERVISION_PRICE"

    page.send(sender_id, Template.Generic([ 
        Template.GenericElement("اشراف ABAT - فني تحليل سلوك تطبيقي", 
                                subtitle="احصل على الاشراف مع متخصيين وخبراء فى تحليل السلوك التطبيقي لتحقيق المتطلب الأول", 
                                image_url="https://github.com/user-attachments/assets/62ebf9cd-048a-4f7a-aa6d-0807422d5322", 
                                buttons = [Template.ButtonWeb("📩  راسلنا واتساب", "https://wa.me/+201152810161?text=مرحبًا، أريد الاستفسار عن إشراف ABAT")]),
        Template.GenericElement("اشراف  QASP-S - مشرف توحد مؤهل", 
                                subtitle="احصل على الاشراف مع متخصيين وخبراء فى تحليل السلوك التطبيقي لتحقيق المتطلب الأول", 
                                image_url="https://github.com/user-attachments/assets/9fd2b39f-dbf0-4f7e-9009-65fe56542e34", 
                                buttons = [Template.ButtonWeb("📩  راسلنا واتساب", "https://wa.me/+201152810161?text=مرحبًا، أريد الاستفسار عن إشراف QASP-S")]),

        Template.GenericElement("اشراف QBA - محلل سلوك مؤهل", 
                                subtitle="احصل على الاشراف مع متخصيين وخبراء فى تحليل السلوك التطبيقي لتحقيق المتطلب الأول", 
                                image_url="https://github.com/user-attachments/assets/719a4380-887b-4a43-a5e6-9da9ca004a45", 
                                buttons = [Template.ButtonWeb("📩  راسلنا واتساب", "https://wa.me/+201152810161?text=مرحبًا، أريد الاستفسار عن إشراف QBA")]),
    ]))

    show_main_menu(sender_id)




def show_platform_approval(sender_id):
    """
    عرض حالة اعتماد المنصة.
    
    Args:
    sender_id (str): معرف المرسل (المستخدم).
    """
    # Update the user's platform approval status
    USER_SEQ[sender_id] = "PLATFORM_APPROVAL"

    # Send the platform approval message
    page.send(sender_id, "نعم، المنصة معتمدة من بورد QABA ✅\n"
                          "ونحن شركاء مع منصة الأبعاد السبعة في السعودية 🇸🇦، حيث يشرف على المنصة فريق من BCBA وQBA معتمدين. 👩‍🎓👨‍🎓\n"
                          "💡 خدماتنا تشمل:\n"
                          "تقديم المتطلب الأول والثاني في ABAT، QASP-S، وQBA.\n"
                          "💰 أسعارنا مخفضة لتتناسب مع السوق المصري، مع الحفاظ على أعلى جودة في التدريب والخدمات. 🏷️✨\n"
                          "🔎 كيف تتأكد من اعتمادية المنصة؟\n"
                          "بمجرد دخولك على موقعنا highnessc.com 🌐، ستجد جميع محللي السلوك والمشرفين مع سيرهم الذاتية.\n"
                          "يمكنك أيضًا زيارة موقع bacb.com/bcba للتأكد بنفسك من اعتمادية المحللين.")
    
    # Correct usage of Template.ButtonWeb
    image_url = "https://github.com/user-attachments/assets/6c299908-b154-4ab3-a3d2-fd0e16e5b911"  # استبدل الرابط بالرابط الصحيح للصورة
    page.send(sender_id, Template.Generic(
        elements=[
            Template.GenericElement(
                title="د/عبد الرحمن القرني",
                subtitle="ماجستير تربية خاصة من Ball State University وطالب دكتوراه في جامعة الملك سعود ومحلل سلوك معتمد BCBA. خبرة 7 سنوات في مجال تحليل السلوك التطبيقي",
                image_url=image_url,
                buttons=[
                    Template.ButtonWeb("شاهد شكل الشهادة", "https://drive.google.com/drive/folders/1CJ7fbCN0cO6DyWs2V8tYMBdFTu4Qiear?usp=drive_link")
                ]
            )
        ]
    ))

    # Show the main menu after sending the information
    show_main_menu(sender_id)




def show_registration_info(sender_id):
    """
    عرض تفاصيل التسجيل في المنصة.
    
    Args:
    sender_id (str): معرف المرسل (المستخدم).
    """
    USER_SEQ[sender_id] = "REGISTRATION"
    
    # Use Template.ButtonWeb correctly
    page.send(sender_id, Template.Buttons(
        text="🎥 اتبع الخطوات فى الفيديو المرفق",
        buttons=[Template.ButtonWeb("اضغط للمشاهدة ▶️", "https://drive.google.com/file/d/1Tu_rt8y-43bs33NuhfyQz_a7U7z3x4SO/view")]
    ))
    show_main_menu(sender_id)




def show_support_options(sender_id):
    """
    عرض خيارات الدعم المتاحة للمستخدم عبر منصات السوشيال ميديا.
    """
    USER_SEQ[sender_id] = "SUPPORT"

    page.send(sender_id, Template.Generic([ 
        Template.GenericElement("فيسبوك", 
                                subtitle="تواصل مع الدعم عبر فيسبوك", 
                                image_url="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg",  
                                buttons=[Template.ButtonWeb("التواصل الآن", "https://m.me/100063887112387"),
                                         Template.ButtonPhoneNumber("اتصل بنا", "+201152810161")]),
        Template.GenericElement("واتساب", 
                                subtitle="تواصل مع الدعم عبر واتساب", 
                                image_url="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg",  
                                buttons=[Template.ButtonWeb("التواصل الآن", "https://wa.me/+201152810161"),
                                         Template.ButtonPhoneNumber("اتصل بنا", "+201152810161")]),
        Template.GenericElement("إنستجرام", 
                                subtitle="تواصل مع الدعم عبر إنستجرام", 
                                image_url="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png",  
                                buttons=[Template.ButtonWeb("التواصل الآن", "https://www.instagram.com/highness.aba/"),
                                         Template.ButtonPhoneNumber("اتصل بنا", "+201152810161")])

    ]))

    show_main_menu(sender_id)






def show_join_info(sender_id):
    USER_SEQ[sender_id] = "JOIN"
    page.send(sender_id, Template.Buttons(
        text="📢 للانضمام إلى المنصة، اضغط على الزر أدناه: 👇",
        buttons=[Template.ButtonWeb("✨ انضم الآن ✨", "https://form.jotform.com/242161912045044")]
    ))    
    show_main_menu(sender_id)



def show_main_menu(sender_id):
    page.send(sender_id, "اختر من الخيارات التالية:", quick_replies=[  
        QuickReply(title="📚 أسعار الكورسات", payload=f"COURSES_PRICE_{sender_id}"),
        QuickReply(title="💡 سعر الاشراف", payload=f"SUPERVISION_PRICE_{sender_id}"),
        QuickReply(title="✅ هل المنصة معتمدة؟", payload=f"PLATFORM_APPROVAL_{sender_id}"),
        QuickReply(title="📝 كيفية التسجيل؟", payload=f"REGISTRATION_{sender_id}"),
        QuickReply(title="🎉 الخصومات المتاحة", payload=f"DISCOUNTS_{sender_id}"),
        QuickReply(title="💬 تواصل مع الدعم", payload=f"SUPPORT_{sender_id}"),
        QuickReply(title="🚀 أريد الانضمام", payload=f"JOIN_{sender_id}")
    ])

# Handling postbacks




@page.handle_postback
def received_postback(event):
    sender_id = event.sender_id
    postback = event.postback
    payload = postback.get('payload') if isinstance(postback, dict) else None

    if payload:
        if "COURSES_PRICE_" in payload:
            show_course_prices(sender_id)
        elif "SUPERVISION_PRICE_" in payload:
            show_supervision_prices(sender_id)
        elif "PLATFORM_APPROVAL_" in payload:
            show_platform_approval(sender_id)
        elif "REGISTRATION_" in payload:
            show_registration_info(sender_id)
        elif "SUPPORT_" in payload:
            show_support_options(sender_id)
        elif "JOIN_" in payload:
            show_join_info(sender_id)
    else:
        print(f"Postback received but no payload: {event}")
