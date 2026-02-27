import React from 'react'
import '../styles/components/_tool-card.scss'

interface Tool {
  id: string | number
  name: string
  description?: string
  url?: string
  category?: string
}

export default function ToolCard({ tool }: { tool: Tool }) {
  return (
    <div className="tool-card">
      <h3 className="tool-card__name">{tool.name}</h3>
      {tool.category && <span className="tool-card__category">{tool.category}</span>}
      {tool.description && <p className="tool-card__description">{tool.description}</p>}
      {tool.url && (
        <a className="tool-card__link" href={tool.url} target="_blank" rel="noopener noreferrer">
          Learn more
        </a>
      )}
    </div>
  )
}
