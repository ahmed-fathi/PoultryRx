import * as mock from './mockApi'
import * as real from './realApi'

const mode = import.meta.env.VITE_API_MODE ?? 'mock'
const impl = mode === 'real' ? real : mock

export const fetchFeatured = impl.fetchFeatured
export const fetchTools = impl.fetchTools
export const fetchBlog = impl.fetchBlog
export const fetchArticle = impl.fetchArticle
export const fetchProfile = impl.fetchProfile
export const fetchLibrary = impl.fetchLibrary
export const fetchFAQ = impl.fetchFAQ
