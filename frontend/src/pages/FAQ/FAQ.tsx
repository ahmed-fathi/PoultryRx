import React from 'react'
import { useQuery } from '@tanstack/react-query'
import { fetchFAQ } from '../../services/mockApi'

export default function FAQ() {
  const { data } = useQuery(['faq'], fetchFAQ)

  return (
    <section className="faq-page">
      <h1>FAQ</h1>
      <ul>
        {data?.results.map((f: any) => (
          <li key={f.id}><strong>{f.question}</strong><p>{f.answer}</p></li>
        ))}
      </ul>
    </section>
  )
}
