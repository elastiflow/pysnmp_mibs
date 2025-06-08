# SNMP MIB module (JANUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/janus_50691/JANUS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:53:06 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Janustech_ObjectIdentity = ObjectIdentity
janustech = _Janustech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50691)
)
_Helium_ObjectIdentity = ObjectIdentity
helium = _Helium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50691, 1)
)
_Ident_ObjectIdentity = ObjectIdentity
ident = _Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50691, 1, 1)
)


class _Fabricante_Type(DisplayString):
    """Custom type fabricante based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Fabricante_Type.__name__ = "DisplayString"
_Fabricante_Object = MibScalar
fabricante = _Fabricante_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 1, 1),
    _Fabricante_Type()
)
fabricante.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabricante.setStatus("mandatory")


class _Modelo_Type(DisplayString):
    """Custom type modelo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Modelo_Type.__name__ = "DisplayString"
_Modelo_Object = MibScalar
modelo = _Modelo_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 1, 2),
    _Modelo_Type()
)
modelo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelo.setStatus("mandatory")


class _Fimware_Type(DisplayString):
    """Custom type fimware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Fimware_Type.__name__ = "DisplayString"
_Fimware_Object = MibScalar
fimware = _Fimware_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 1, 3),
    _Fimware_Type()
)
fimware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fimware.setStatus("mandatory")


class _Agent_Type(DisplayString):
    """Custom type agent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Agent_Type.__name__ = "DisplayString"
_Agent_Object = MibScalar
agent = _Agent_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 1, 4),
    _Agent_Type()
)
agent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent.setStatus("mandatory")
_StatusPacket_ObjectIdentity = ObjectIdentity
statusPacket = _StatusPacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2)
)
_AnalogValues_ObjectIdentity = ObjectIdentity
analogValues = _AnalogValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 1)
)
_Pressao_Type = Integer32
_Pressao_Object = MibScalar
pressao = _Pressao_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 1, 1),
    _Pressao_Type()
)
pressao.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressao.setStatus("mandatory")
_Temperatura_Type = Integer32
_Temperatura_Object = MibScalar
temperatura = _Temperatura_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 1, 2),
    _Temperatura_Type()
)
temperatura.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatura.setStatus("mandatory")
_Umidade_Type = Integer32
_Umidade_Object = MibScalar
umidade = _Umidade_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 1, 3),
    _Umidade_Type()
)
umidade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umidade.setStatus("mandatory")
_StatusPacketAlarms_ObjectIdentity = ObjectIdentity
statusPacketAlarms = _StatusPacketAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 2)
)


class _Runstatus_Type(Integer32):
    """Custom type runstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Runstatus_Type.__name__ = "Integer32"
_Runstatus_Object = MibScalar
runstatus = _Runstatus_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 2, 1),
    _Runstatus_Type()
)
runstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runstatus.setStatus("mandatory")


class _Motortemperror_Type(Integer32):
    """Custom type motortemperror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Motortemperror_Type.__name__ = "Integer32"
_Motortemperror_Object = MibScalar
motortemperror = _Motortemperror_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 2, 2),
    _Motortemperror_Type()
)
motortemperror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motortemperror.setStatus("mandatory")


class _Solenoidopen_Type(Integer32):
    """Custom type solenoidopen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Solenoidopen_Type.__name__ = "Integer32"
_Solenoidopen_Object = MibScalar
solenoidopen = _Solenoidopen_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 2, 3),
    _Solenoidopen_Type()
)
solenoidopen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solenoidopen.setStatus("mandatory")


class _Powererror_Type(Integer32):
    """Custom type powererror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Powererror_Type.__name__ = "Integer32"
_Powererror_Object = MibScalar
powererror = _Powererror_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 2, 4),
    _Powererror_Type()
)
powererror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powererror.setStatus("mandatory")


class _Highwatertemp_Type(Integer32):
    """Custom type highwatertemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Highwatertemp_Type.__name__ = "Integer32"
_Highwatertemp_Object = MibScalar
highwatertemp = _Highwatertemp_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 2, 5),
    _Highwatertemp_Type()
)
highwatertemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highwatertemp.setStatus("mandatory")


class _Lowwaterflow_Type(Integer32):
    """Custom type lowwaterflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Lowwaterflow_Type.__name__ = "Integer32"
_Lowwaterflow_Object = MibScalar
lowwaterflow = _Lowwaterflow_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 2, 6),
    _Lowwaterflow_Type()
)
lowwaterflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowwaterflow.setStatus("mandatory")


class _Gastemperror_Type(Integer32):
    """Custom type gastemperror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Gastemperror_Type.__name__ = "Integer32"
_Gastemperror_Object = MibScalar
gastemperror = _Gastemperror_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 2, 7),
    _Gastemperror_Type()
)
gastemperror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gastemperror.setStatus("mandatory")


class _Lowpressureshutdown_Type(Integer32):
    """Custom type lowpressureshutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Lowpressureshutdown_Type.__name__ = "Integer32"
_Lowpressureshutdown_Object = MibScalar
lowpressureshutdown = _Lowpressureshutdown_Object(
    (1, 3, 6, 1, 4, 1, 50691, 1, 2, 2, 8),
    _Lowpressureshutdown_Type()
)
lowpressureshutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpressureshutdown.setStatus("mandatory")
_AlarmDefinition_ObjectIdentity = ObjectIdentity
alarmDefinition = _AlarmDefinition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50691, 1, 3)
)
_HeliumTraps_ObjectIdentity = ObjectIdentity
heliumTraps = _HeliumTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20)
)

# Managed Objects groups


# Notification objects

alarmeRunstatusALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 1)
)
if mibBuilder.loadTexts:
    alarmeRunstatusALARM.setStatus(
        ""
    )

alarmeRunstatusNORMAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 2)
)
if mibBuilder.loadTexts:
    alarmeRunstatusNORMAL.setStatus(
        ""
    )

alarmeMotortemperrorALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 3)
)
if mibBuilder.loadTexts:
    alarmeMotortemperrorALARM.setStatus(
        ""
    )

alarmeMotortemperrorNORMAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 4)
)
if mibBuilder.loadTexts:
    alarmeMotortemperrorNORMAL.setStatus(
        ""
    )

alarmeSolenoidopenALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 5)
)
if mibBuilder.loadTexts:
    alarmeSolenoidopenALARM.setStatus(
        ""
    )

alarmeSolenoidopenNORMAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 6)
)
if mibBuilder.loadTexts:
    alarmeSolenoidopenNORMAL.setStatus(
        ""
    )

alarmePowererrorALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 7)
)
if mibBuilder.loadTexts:
    alarmePowererrorALARM.setStatus(
        ""
    )

alarmePowererrorNORMAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 8)
)
if mibBuilder.loadTexts:
    alarmePowererrorNORMAL.setStatus(
        ""
    )

alarmeHighwatertempALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 9)
)
if mibBuilder.loadTexts:
    alarmeHighwatertempALARM.setStatus(
        ""
    )

alarmeHighwatertempNORMAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 10)
)
if mibBuilder.loadTexts:
    alarmeHighwatertempNORMAL.setStatus(
        ""
    )

alarmeLowwaterflowALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 11)
)
if mibBuilder.loadTexts:
    alarmeLowwaterflowALARM.setStatus(
        ""
    )

alarmeLowwaterflowNORMAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 12)
)
if mibBuilder.loadTexts:
    alarmeLowwaterflowNORMAL.setStatus(
        ""
    )

alarmeGastemperrorALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 13)
)
if mibBuilder.loadTexts:
    alarmeGastemperrorALARM.setStatus(
        ""
    )

alarmeGastemperrorNORMAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 14)
)
if mibBuilder.loadTexts:
    alarmeGastemperrorNORMAL.setStatus(
        ""
    )

alarmeLowpressureshutdownALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 15)
)
if mibBuilder.loadTexts:
    alarmeLowpressureshutdownALARM.setStatus(
        ""
    )

alarmeLowpressureshutdownNORMAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 50691, 1, 20, 0, 16)
)
if mibBuilder.loadTexts:
    alarmeLowpressureshutdownNORMAL.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JANUS-MIB",
    **{"janustech": janustech,
       "helium": helium,
       "ident": ident,
       "fabricante": fabricante,
       "modelo": modelo,
       "fimware": fimware,
       "agent": agent,
       "statusPacket": statusPacket,
       "analogValues": analogValues,
       "pressao": pressao,
       "temperatura": temperatura,
       "umidade": umidade,
       "statusPacketAlarms": statusPacketAlarms,
       "runstatus": runstatus,
       "motortemperror": motortemperror,
       "solenoidopen": solenoidopen,
       "powererror": powererror,
       "highwatertemp": highwatertemp,
       "lowwaterflow": lowwaterflow,
       "gastemperror": gastemperror,
       "lowpressureshutdown": lowpressureshutdown,
       "alarmDefinition": alarmDefinition,
       "heliumTraps": heliumTraps,
       "alarmeRunstatusALARM": alarmeRunstatusALARM,
       "alarmeRunstatusNORMAL": alarmeRunstatusNORMAL,
       "alarmeMotortemperrorALARM": alarmeMotortemperrorALARM,
       "alarmeMotortemperrorNORMAL": alarmeMotortemperrorNORMAL,
       "alarmeSolenoidopenALARM": alarmeSolenoidopenALARM,
       "alarmeSolenoidopenNORMAL": alarmeSolenoidopenNORMAL,
       "alarmePowererrorALARM": alarmePowererrorALARM,
       "alarmePowererrorNORMAL": alarmePowererrorNORMAL,
       "alarmeHighwatertempALARM": alarmeHighwatertempALARM,
       "alarmeHighwatertempNORMAL": alarmeHighwatertempNORMAL,
       "alarmeLowwaterflowALARM": alarmeLowwaterflowALARM,
       "alarmeLowwaterflowNORMAL": alarmeLowwaterflowNORMAL,
       "alarmeGastemperrorALARM": alarmeGastemperrorALARM,
       "alarmeGastemperrorNORMAL": alarmeGastemperrorNORMAL,
       "alarmeLowpressureshutdownALARM": alarmeLowpressureshutdownALARM,
       "alarmeLowpressureshutdownNORMAL": alarmeLowpressureshutdownNORMAL}
)
