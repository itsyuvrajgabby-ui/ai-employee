from sqlalchemy.orm import Session

from ..models import KnowledgeDocument


def get_company_knowledge(
    db: Session,
    company_id: int,
    query: str,
) -> str:

    documents = (
        db.query(KnowledgeDocument)
        .filter(
            KnowledgeDocument.company_id == company_id
        )
        .all()
    )

    if not documents:
        return "No company knowledge has been uploaded."

    query_words = set(query.lower().split())

    matches = []

    for document in documents:

        words = set(document.content.lower().split())

        score = len(
            query_words.intersection(words)
        )

        if score > 0:
            matches.append(
                (score, document)
            )

    matches.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    selected = matches[:5]

    if not selected:
        selected = [
            (0, document)
            for document in documents[:5]
        ]

    return "\n\n".join(
        f"DOCUMENT: {document.filename}\n"
        f"{document.content}"
        for _, document in selected
    )
