import { z } from 'zod'

// Auth Schemas
export const loginSchema = z.object({
  email: z
    .string()
    .email('Please enter a valid email address')
    .min(1, 'Email is required'),
  password: z.string().min(1, 'Password is required'),
})

export const signupSchema = z
  .object({
    email: z
      .string()
      .email('Please enter a valid email address')
      .min(1, 'Email is required'),
    username: z
      .string()
      .min(3, 'Username must be at least 3 characters')
      .max(32, 'Username must be less than 32 characters')
      .regex(
        /^[a-zA-Z0-9_-]+$/,
        'Username can only contain letters, numbers, underscores, and hyphens'
      ),
    password: z
      .string()
      .min(8, 'Password must be at least 8 characters')
      .regex(/[A-Z]/, 'Password must contain at least one uppercase letter')
      .regex(/[0-9]/, 'Password must contain at least one number'),
    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: 'Passwords do not match',
    path: ['confirmPassword'],
  })

export const forgotPasswordSchema = z.object({
  email: z
    .string()
    .email('Please enter a valid email address')
    .min(1, 'Email is required'),
})

export const resetPasswordSchema = z
  .object({
    password: z
      .string()
      .min(8, 'Password must be at least 8 characters')
      .regex(/[A-Z]/, 'Password must contain at least one uppercase letter')
      .regex(/[0-9]/, 'Password must contain at least one number'),
    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: 'Passwords do not match',
    path: ['confirmPassword'],
  })

export const emailVerificationSchema = z.object({
  email: z
    .string()
    .email('Please enter a valid email address')
    .min(1, 'Email is required'),
  code: z.string().min(6, 'Verification code is required'),
})

export const otpSchema = z.object({
  otp: z
    .string()
    .length(6, 'OTP must be 6 characters')
    .regex(/^\d+$/, 'OTP must contain only numbers'),
})

// Profile Schemas
export const updateProfileSchema = z.object({
  username: z
    .string()
    .min(3, 'Username must be at least 3 characters')
    .max(32, 'Username must be less than 32 characters')
    .optional(),
  email: z.string().email('Please enter a valid email address').optional(),
})

// Test Response Schemas
export const testResponseSchema = z.record(
  z.string(),
  z.number().int().min(0).max(3)
)

export type LoginInput = z.infer<typeof loginSchema>
export type SignupInput = z.infer<typeof signupSchema>
export type ForgotPasswordInput = z.infer<typeof forgotPasswordSchema>
export type ResetPasswordInput = z.infer<typeof resetPasswordSchema>
export type EmailVerificationInput = z.infer<typeof emailVerificationSchema>
export type OTPInput = z.infer<typeof otpSchema>
export type UpdateProfileInput = z.infer<typeof updateProfileSchema>
export type TestResponseInput = z.infer<typeof testResponseSchema>
