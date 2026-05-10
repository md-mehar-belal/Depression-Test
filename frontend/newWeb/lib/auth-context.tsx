'use client'

import React, { createContext, useContext, useState, useCallback, useEffect } from 'react'
import { UserProfile, AuthContextType } from './types'
import axios from 'axios'

const AuthContext = createContext<AuthContextType | undefined>(undefined)

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3001/api'

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<UserProfile | null>(null)
  const [loading, setLoading] = useState(true)
  const [isAuthenticated, setIsAuthenticated] = useState(false)

  // Initialize auth state from token
  useEffect(() => {
    const initializeAuth = async () => {
      try {
        const token = localStorage.getItem('authToken')
        if (token) {
          // Validate token with backend
          const response = await axios.get(`${API_BASE_URL}/auth/me`, {
            headers: { Authorization: `Bearer ${token}` },
          })
          setUser(response.data.user)
          setIsAuthenticated(true)
        }
      } catch (error) {
        localStorage.removeItem('authToken')
        setUser(null)
        setIsAuthenticated(false)
      } finally {
        setLoading(false)
      }
    }

    initializeAuth()
  }, [])

  const login = useCallback(async (email: string, password: string) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/auth/login`, {
        email,
        password,
      })
      const { token, user: userData } = response.data
      localStorage.setItem('authToken', token)
      setUser(userData)
      setIsAuthenticated(true)
    } catch (error) {
      throw error
    }
  }, [])

  const signup = useCallback(
    async (email: string, username: string, password: string) => {
      try {
        const response = await axios.post(`${API_BASE_URL}/auth/signup`, {
          email,
          username,
          password,
        })
        const { token, user: userData } = response.data
        localStorage.setItem('authToken', token)
        setUser(userData)
        setIsAuthenticated(true)
      } catch (error) {
        throw error
      }
    },
    []
  )

  const logout = useCallback(async () => {
    try {
      const token = localStorage.getItem('authToken')
      if (token) {
        await axios.post(
          `${API_BASE_URL}/auth/logout`,
          {},
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        )
      }
    } catch (error) {
      console.error('Logout error:', error)
    } finally {
      localStorage.removeItem('authToken')
      setUser(null)
      setIsAuthenticated(false)
    }
  }, [])

  const googleLogin = useCallback(async (token: string) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/auth/google`, {
        token,
      })
      const { token: authToken, user: userData } = response.data
      localStorage.setItem('authToken', authToken)
      setUser(userData)
      setIsAuthenticated(true)
    } catch (error) {
      throw error
    }
  }, [])

  const forgotPassword = useCallback(async (email: string) => {
    try {
      await axios.post(`${API_BASE_URL}/auth/forgot-password`, { email })
    } catch (error) {
      throw error
    }
  }, [])

  const resetPassword = useCallback(
    async (email: string, code: string, password: string) => {
      try {
        const response = await axios.post(
          `${API_BASE_URL}/auth/reset-password`,
          {
            email,
            code,
            password,
          }
        )
        const { token, user: userData } = response.data
        localStorage.setItem('authToken', token)
        setUser(userData)
        setIsAuthenticated(true)
      } catch (error) {
        throw error
      }
    },
    []
  )

  const value: AuthContextType = {
    user,
    isAuthenticated,
    loading,
    login,
    signup,
    logout,
    googleLogin,
    forgotPassword,
    resetPassword,
  }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}
