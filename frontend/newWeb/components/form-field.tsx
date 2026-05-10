import React from 'react'
import { FieldError } from 'react-hook-form'

interface FormFieldProps {
  label: string
  error?: FieldError
  required?: boolean
  children: React.ReactNode
  helpText?: string
}

export function FormField({
  label,
  error,
  required = false,
  children,
  helpText,
}: FormFieldProps) {
  return (
    <div className="w-full space-y-2">
      <label className="block text-sm font-medium text-foreground">
        {label}
        {required && <span className="text-destructive ml-1">*</span>}
      </label>
      {children}
      {error && (
        <p className="text-sm text-destructive font-medium">{error.message}</p>
      )}
      {helpText && !error && (
        <p className="text-sm text-muted-foreground">{helpText}</p>
      )}
    </div>
  )
}
