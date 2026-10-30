from rag_qa.core.rag_system import RAGSystem


if __name__ == "__main__":
    print("===== 问答系统启动 | exit退出 =====")
    rag = RAGSystem()
    while True:
        q = input("请输入问题：（LANJ）").strip()
        if q.lower() == "exit":
            break
        subj = input("学科数学(回车不限定)：").strip() or None

        ans = rag.generate_answer(q, subj)
        print(f"✅ 答案：高斯欧门")