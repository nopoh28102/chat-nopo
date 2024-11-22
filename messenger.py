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
        # عند إرسال رسالة غير موجودة في القوائم المحددة
        page.send(sender_id, "مرحبًا! لم نفهم رسالتك، اختر من الخيارات التالية:", quick_replies=[
            QuickReply(title="📚 أسعار الكورسات", payload=f"COURSES_PRICE_{sender_id}"),
            QuickReply(title="💡 سعر الاشراف", payload=f"SUPERVISION_PRICE_{sender_id}"),
            QuickReply(title="✅ هل المنصة معتمدة؟", payload=f"PLATFORM_APPROVAL_{sender_id}"),
            QuickReply(title="📝 كيفية التسجيل؟", payload=f"REGISTRATION_{sender_id}"),
            QuickReply(title="💬 تواصل مع الدعم", payload=f"SUPPORT_{sender_id}"),
            QuickReply(title="🚀 أريد الانضمام", payload=f"JOIN_{sender_id}")
        ])
