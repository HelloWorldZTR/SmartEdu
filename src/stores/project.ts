import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { Project, Job } from '@/types'
import { projectApi } from '@/api/project'

export const useProjectStore = defineStore('project', () => {
  const projects = ref<Project[]>([])
  const currentProject = ref<Project | null>(null)
  const isLoading = ref(false)
  const filters = ref({
    category: '',
    skills: [] as string[],
    salaryRange: '',
    targetAudience: ''
  })

  // 计算属性
  const filteredProjects = computed(() => {
    let filtered = projects.value

    if (filters.value.category) {
      filtered = filtered.filter(project => 
        project.tags.includes(filters.value.category)
      )
    }

    if (filters.value.skills.length > 0) {
      filtered = filtered.filter(project =>
        project.jobs.some(job => {
          const skills = job.requiredSkills || job.required_skills || []
          return skills.some(skill =>
            filters.value.skills.includes(skill)
          )
        })
      )
    }

    if (filters.value.targetAudience) {
      filtered = filtered.filter(project =>
        project.targetAudience === filters.value.targetAudience
      )
    }

    return filtered
  })

  const recruitingProjects = computed(() =>
    projects.value.filter(project => project.status === 'recruiting')
  )

  // Actions
  const fetchProjects = async (params?: {
    page?: number
    pageSize?: number
    category?: string
  }) => {
    try {
      isLoading.value = true
      const response = await projectApi.getProjects(params)
      projects.value = response.results || []
      return response
    } catch (error) {
      throw error
    } finally {
      isLoading.value = false
    }
  }

  const fetchProjectById = async (id: number) => {
    try {
      isLoading.value = true
      const response = await projectApi.getProjectById(id)
      currentProject.value = response
      return response
    } catch (error) {
      throw error
    } finally {
      isLoading.value = false
    }
  }

  const createProject = async (projectData: {
    title: string
    description: string
    targetAudience: 'school' | 'department' | 'national'
    tags: string[]
    jobs: Omit<Job, 'id' | 'applications'>[]
  }) => {
    try {
      isLoading.value = true
      const response = await projectApi.createProject(projectData)
      projects.value.unshift(response.data)
      return response.data
    } catch (error) {
      throw error
    } finally {
      isLoading.value = false
    }
  }

  const updateProject = async (id: number, projectData: Partial<Project>) => {
    try {
      isLoading.value = true
      const response = await projectApi.updateProject(id, projectData)
      const index = projects.value.findIndex(p => p.id === id)
      if (index !== -1) {
        projects.value[index] = response.data
      }
      if (currentProject.value?.id === id) {
        currentProject.value = response.data
      }
      return response.data
    } catch (error) {
      throw error
    } finally {
      isLoading.value = false
    }
  }

  const deleteProject = async (id: number) => {
    try {
      await projectApi.deleteProject(id)
      projects.value = projects.value.filter(p => p.id !== id)
      if (currentProject.value?.id === id) {
        currentProject.value = null
      }
    } catch (error) {
      throw error
    }
  }

  const applyToJob = async (projectId: number, jobId: number, applicationData: {
    resumeId: number
    note?: string
  }) => {
    try {
      const response = await projectApi.applyToJob(projectId, jobId, applicationData)
      // 更新当前项目的申请状态
      if (currentProject.value?.id === projectId) {
        const job = currentProject.value.jobs.find(j => j.id === jobId)
        if (job) {
          job.applications.push(response.data)
        }
      }
      return response.data
    } catch (error) {
      throw error
    }
  }

  const setFilters = (newFilters: Partial<typeof filters.value>) => {
    filters.value = { ...filters.value, ...newFilters }
  }

  const clearFilters = () => {
    filters.value = {
      category: '',
      skills: [],
      salaryRange: '',
      targetAudience: ''
    }
  }

  return {
    // State
    projects,
    currentProject,
    isLoading,
    filters,
    
    // Getters
    filteredProjects,
    recruitingProjects,
    
    // Actions
    fetchProjects,
    fetchProjectById,
    createProject,
    updateProject,
    deleteProject,
    applyToJob,
    setFilters,
    clearFilters
  }
}) 