// src/lib/api.ts

export type Service = {
  id: number;
  name: string;
  description?: string;
  price: number;
};




export type ServiceForPdf = {
  name: string;
  description?: string;
  price: number;
};

export type GeneratePdfRequest = {
  client_name: string;
  company_name: string;
  discount: number;
  services: ServiceForPdf[];
};


export async function fetchServices(): Promise<Service[]> {
  const res = await fetch('http://localhost:8000/services');
  if (!res.ok) throw new Error('Ошибка получения услуг');
  return res.json();
}

export async function generatePdf(data: GeneratePdfRequest): Promise<Blob> {
  const res = await fetch('http://localhost:8000/generate-pdf', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error('Ошибка генерации PDF');
  return res.blob();
}
