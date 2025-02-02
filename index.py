import time

def level_1():
    print("\n--- مستوى محمد حالات ---")
    print("السؤال الأول:")
    print("ما هو الشيء الذي يمشي بلا رجلين ويبكي بلا عينين؟")
    answer = input("الإجابة: ").strip().lower()
    
    if answer == "السحاب" or answer == "الغمام":
        print("إجابة صحيحة! تنتقل للمستوى التالي 🎉")
        return True
    else:
        print("إجابة خاطئة! حاول مرة أخرى ❌")
        return False

def level_2():
    print("\n--- مستوى عومر جمول ---")
    print("السؤال الثاني:")
    print("أخو خالتك وابن عمتك وليس بأختك، فمن يكون؟")
    answer = input("الإجابة: ").strip().lower()
    
    if answer == "ابني" or answer == "ابنك":
        print("إجابة صحيحة! تهانينا، وصلت للمستوى الأخير 🔥")
        return True
    else:
        print("إجابة خاطئة! جرب مرة أخرى ❌")
        return False

def level_3():
    print("\n--- مستوى لو كسبت تستحق لقب عمرو المجتمع ---")
    print("السؤال الثالث (لديك 15 ثانية فقط):")
    print("أرقام متتالية مجموعها 15، ما هي؟ (مثال: 1+2+3... الخ)")
    
    start_time = time.time()
    answer = input("الإجابة (أدخل الأرقام متتالية مثل 1+2+3): ").strip()
    end_time = time.time()
    
    if end_time - start_time > 15:
        print("انتهى الوقت! فشلت في المستوى ⏳")
        return False
    
    numbers = list(map(int, answer.split('+')))
    
    # التحقق من أن الأرقام متتالية ومجموعها 15
    if all(numbers[i]+1 == numbers[i+1] for i in range(len(numbers)-1)) and sum(numbers) == 15:
        print("إجابة صحيحة! أنت عبقرية 🤯 تـســتــحــق لقب عمرو المجتمع!")
        return True
    else:
        print("إجابة خاطئة! المستوى صعب لكن حاول مرة أخرى 💪")
        return False

def main():
    print("مرحبا بكم في لعبة الألغاز الذكية!")
    print("يجب أن تجتاز جميع المستويات لتفوز باللقب\n")
    
    if not level_1():
        return
    
    if not level_2():
        return
    
    if level_3():
        print("\n🎊🎊🎊 فـــوز كــبــيــر! أنت أسطورة الألغاز! 🎊🎊🎊")
    else:
        print("\nللأسف لم تنجح في المستوى الأخير، حاول مرة أخرى!")

if __name__ == "__main__":
    main()
