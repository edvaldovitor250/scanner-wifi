<body>
  <div style="max-width: 800px; margin: 40px auto; padding: 30px; background: #fff; border-radius: 12px; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1); font-family: 'Roboto', Arial, sans-serif;">
    <h1 style="font-size: 32px; color: #333;">scanner-wifi 🚀📡</h1>
    <p>Uma aplicação simples para escanear dispositivos na rede Wi-Fi com interface web, login e estilização moderna! 😎</p>
    <h2 style="font-size: 24px; color: #444;">Visão Geral ✨</h2>
    <p>
      O <strong>scanner-wifi</strong> é uma aplicação Flask que utiliza o Nmap para identificar dispositivos conectados à sua rede e detectar o sistema operacional de cada um. Possui:
    </p>
    <ul>
      <li>Tela de login com dados fixos 🔒</li>
      <li>Interface principal para escanear a rede e exibir resultados 📊</li>
      <li>Estilização separada com CSS para uma experiência visual aprimorada 🎨</li>
    </ul>
    <h2 style="font-size: 24px; color: #444;">Funcionalidades ⚙️</h2>
    <ul>
      <li><strong>Login Seguro:</strong> Acesso restrito com credenciais fixas (usuário: <code>admin</code>, senha: <code>senha123</code>)</li>
      <li><strong>Escaneamento de Rede:</strong> Varredura de IPs na faixa definida para identificar dispositivos ativos</li>
      <li><strong>Detecção de SO:</strong> Identifica o sistema operacional de cada dispositivo encontrado</li>
      <li><strong>Interface Web Interativa:</strong> Design moderno com efeitos de hover, transições e layout responsivo</li>
    </ul>
    <h2 style="font-size: 24px; color: #444;">Estrutura do Projeto 📁</h2>
    <pre style="background: #f5f5f5; padding: 15px; border-radius: 6px;">
scanner-wifi/
├── app.py
├── scanner/
│   ├── __init__.py
│   ├── os_detector.py
│   └── network_scanner.py
├── templates/
│   ├── login.html
│   └── index.html
└── static/
    ├── login.css
    └── main.css
    </pre>
    <h2 style="font-size: 24px; color: #444;">Instalação & Execução 🚀</h2>
    <ol>
      <li>
        <strong>Clone o repositório:</strong>
        <pre style="background: #f5f5f5; padding: 10px; border-radius: 6px;">git clone https://github.com/seu-usuario/scanner-wifi.git
cd scanner-wifi</pre>
      </li>
      <li>
        <strong>Instale as dependências:</strong>
        <pre style="background: #f5f5f5; padding: 10px; border-radius: 6px;">pip install python-nmap flask</pre>
      </li>
      <li>
        <strong>Instale o Nmap:</strong>
        Certifique-se de que o Nmap esteja instalado no seu sistema. Baixe em: <a href="https://nmap.org/download.html" target="_blank">https://nmap.org/download.html</a>
      </li>
      <li>
        <strong>Execute a aplicação:</strong>
        <pre style="background: #f5f5f5; padding: 10px; border-radius: 6px;">python app.py</pre>
        Acesse <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a> no seu navegador.
      </li>
    </ol>
    <h2 style="font-size: 24px; color: #444;">Como Usar 👨‍💻</h2>
    <ol>
      <li>
        <strong>Login:</strong> Acesse a tela de login e entre com:
        <ul>
          <li>Usuário: <code>admin</code></li>
          <li>Senha: <code>senha123</code></li>
        </ul>
      </li>
      <li>
        <strong>Escanear a Rede:</strong> Após o login, insira a faixa de IP (por exemplo, <code>192.168.0.0/24</code>) e clique em <strong>Scan</strong>.
      </li>
      <li>
        <strong>Visualizar Resultados:</strong> Os dispositivos ativos e seus sistemas operacionais serão listados na tela.
      </li>
    </ol>
    <h2 style="font-size: 24px; color: #444;">Personalização 🎨</h2>
    <ul>
      <li>
        <strong>CSS:</strong> Os estilos da aplicação estão separados em dois arquivos:
        <ul>
          <li><code>static/login.css</code> para a tela de login.</li>
          <li><code>static/main.css</code> para a interface principal.</li>
        </ul>
      </li>
      <li>
        <strong>Funcionalidades:</strong> Você pode expandir a aplicação adicionando mais funcionalidades, como:
        <ul>
          <li>Detalhamento dos dispositivos encontrados.</li>
          <li>Exportação dos resultados para CSV ou PDF.</li>
          <li>Melhoria na detecção de SO com técnicas mais avançadas.</li>
        </ul>
      </li>
    </ul>
    <h2 style="font-size: 24px; color: #444;">Contribuição 🤝</h2>
    <p>Sinta-se à vontade para contribuir! Siga os passos abaixo:</p>
    <ol>
      <li>Faça um fork do projeto.</li>
      <li>Crie uma branch para sua feature (<code>git checkout -b minha-nova-feature</code>).</li>
      <li>Faça commit das suas alterações (<code>git commit -am 'Adiciona nova feature'</code>).</li>
      <li>Envie a branch (<code>git push origin minha-nova-feature</code>).</li>
      <li>Abra um Pull Request.</li>
    </ol>
    <h2 style="font-size: 24px; color: #444;">Licença 📄</h2>
    <p>Este projeto está licenciado sob a <a href="LICENSE" target="_blank">MIT License</a>.</p>
    <hr style="margin: 30px 0;">
    <p style="text-align: center;">Aproveite e boa varredura! 🔍📶</p>
  </div>
</body>
