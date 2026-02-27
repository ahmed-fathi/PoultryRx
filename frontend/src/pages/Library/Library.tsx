import React from 'react'
import { useQuery } from '@tanstack/react-query'
import { fetchLibrary } from '../../services/mockApi'

export default function Library() {
  const { data } = useQuery(['library'], fetchLibrary)

  return (
    <section className="library-page">
      <h1>Library</h1>
      <ul>
        {data?.results.map((r: any) => (
          <li key={r.id}><a href={r.mock_download_url}>{r.title} ({r.type})</a></li>
        ))}
      </ul>
    </section>
  )
}
