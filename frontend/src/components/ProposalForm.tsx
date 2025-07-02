'use client';

import { useEffect, useState } from 'react';
import { fetchServices, generatePdf, Service, ServiceForPdf } from '../lib/api';

export default function ProposalForm() {
  const [services, setServices] = useState<Service[]>([]);
  const [selected, setSelected] = useState<number[]>([]);
  const [client, setClient] = useState('');
  const [company, setCompany] = useState('');
  const [discount, setDiscount] = useState(0);

  useEffect(() => {
    fetchServices().then(setServices).catch(() => setServices([]));
  }, []);

  const handleToggle = (id: number) => {
    setSelected(selected =>
      selected.includes(id) ? selected.filter(s => s !== id) : [...selected, id]
    );
  };

  
  const chosenServices: ServiceForPdf[] = services
    .filter(s => selected.includes(s.id))
    .map(({ name, description, price }) => ({ name, description, price }));

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!client || !company || chosenServices.length === 0) {
      alert('Заполните все поля и выберите услугу');
      return;
    }
    try {
      const pdf = await generatePdf({
        client_name: client,
        company_name: company,
        discount,
        services: chosenServices,
      });
      const url = window.URL.createObjectURL(pdf);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'proposal.pdf';
      a.click();
      window.URL.revokeObjectURL(url);
    } catch {
      alert('Ошибка генерации PDF');
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-[#282c36] rounded-xl shadow-lg p-6 sm:p-8 mb-10 border border-[#3b4255] space-y-5"
    >
      <div className="flex flex-col gap-3">
        <input
          placeholder="Client name"
          className="w-full bg-[#22242b] text-white border border-[#4f46e5] rounded px-3 py-2 focus:outline-none focus:border-yellow-400 transition"
          value={client}
          onChange={e => setClient(e.target.value)}
        />
        <input
          placeholder="Company"
          className="w-full bg-[#22242b] text-white border border-[#4f46e5] rounded px-3 py-2 focus:outline-none focus:border-yellow-400 transition"
          value={company}
          onChange={e => setCompany(e.target.value)}
        />
        <input
          type="number"
          placeholder="Discount %"
          className="w-full bg-[#22242b] text-white border border-[#4f46e5] rounded px-3 py-2 focus:outline-none focus:border-yellow-400 transition"
          value={discount}
          min={0}
          max={100}
          onChange={e => setDiscount(Number(e.target.value))}
        />
      </div>
      <div>
        <div className="mb-2 font-semibold text-yellow-400">Services:</div>
        <div className="space-y-2">
          {services.map(s => (
            <label
              key={s.id}
              className="flex items-center gap-2 bg-[#232146] p-2 rounded-md border border-[#3b4255] hover:border-yellow-400 transition"
            >
              <input
                type="checkbox"
                checked={selected.includes(s.id)}
                onChange={() => handleToggle(s.id)}
                className="accent-yellow-400"
              />
              <span className="font-medium text-white">{s.name}</span>
              <span className="text-xs text-indigo-200">{s.description}</span>
              <span className="ml-auto text-yellow-300 font-semibold">{s.price} €</span>
            </label>
          ))}
        </div>
      </div>
      <button
        type="submit"
        className="w-full bg-yellow-400 hover:bg-yellow-300 text-[#232146] font-bold py-2 rounded-lg mt-2 transition"
      >
        Download PDF
      </button>
      <div className="text-xs text-indigo-200 mt-2">
        Email delivery is available in production only
      </div>
    </form>
  );
}
