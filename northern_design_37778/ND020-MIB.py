# SNMP MIB module (ND020-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/northern_design_37778/ND020-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:51:14 2025
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

ndMeter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37778)
)
if mibBuilder.loadTexts:
    ndMeter.setRevisions(
        ("2011-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MeterkWhH_Type = Unsigned32
_MeterkWhH_Object = MibScalar
meterkWhH = _MeterkWhH_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7680),
    _MeterkWhH_Type()
)
meterkWhH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterkWhH.setStatus("current")
if mibBuilder.loadTexts:
    meterkWhH.setUnits("kWh")
_MeterkWhL_Type = Unsigned32
_MeterkWhL_Object = MibScalar
meterkWhL = _MeterkWhL_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7681),
    _MeterkWhL_Type()
)
meterkWhL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterkWhL.setStatus("current")
if mibBuilder.loadTexts:
    meterkWhL.setUnits("kWh")
_MeterkVAhH_Type = Unsigned32
_MeterkVAhH_Object = MibScalar
meterkVAhH = _MeterkVAhH_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7682),
    _MeterkVAhH_Type()
)
meterkVAhH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterkVAhH.setStatus("current")
if mibBuilder.loadTexts:
    meterkVAhH.setUnits("kVAh")
_MeterkVAhL_Type = Unsigned32
_MeterkVAhL_Object = MibScalar
meterkVAhL = _MeterkVAhL_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7683),
    _MeterkVAhL_Type()
)
meterkVAhL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterkVAhL.setStatus("current")
if mibBuilder.loadTexts:
    meterkVAhL.setUnits("kVAh")
_MeterkvarhH_Type = Unsigned32
_MeterkvarhH_Object = MibScalar
meterkvarhH = _MeterkvarhH_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7684),
    _MeterkvarhH_Type()
)
meterkvarhH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterkvarhH.setStatus("current")
if mibBuilder.loadTexts:
    meterkvarhH.setUnits("kvarh")
_MeterkvarhL_Type = Unsigned32
_MeterkvarhL_Object = MibScalar
meterkvarhL = _MeterkvarhL_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7685),
    _MeterkvarhL_Type()
)
meterkvarhL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterkvarhL.setStatus("current")
if mibBuilder.loadTexts:
    meterkvarhL.setUnits("kvarh")
_MeterEkWhH_Type = Unsigned32
_MeterEkWhH_Object = MibScalar
meterEkWhH = _MeterEkWhH_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7686),
    _MeterEkWhH_Type()
)
meterEkWhH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterEkWhH.setStatus("current")
if mibBuilder.loadTexts:
    meterEkWhH.setUnits("kvarh")
_MeterEkWhL_Type = Unsigned32
_MeterEkWhL_Object = MibScalar
meterEkWhL = _MeterEkWhL_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7687),
    _MeterEkWhL_Type()
)
meterEkWhL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterEkWhL.setStatus("current")
if mibBuilder.loadTexts:
    meterEkWhL.setUnits("kvarh")
_MeterP1Amps_Type = Unsigned32
_MeterP1Amps_Object = MibScalar
meterP1Amps = _MeterP1Amps_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7688),
    _MeterP1Amps_Type()
)
meterP1Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP1Amps.setStatus("current")
if mibBuilder.loadTexts:
    meterP1Amps.setUnits("Amps")
_MeterP2Amps_Type = Unsigned32
_MeterP2Amps_Object = MibScalar
meterP2Amps = _MeterP2Amps_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7689),
    _MeterP2Amps_Type()
)
meterP2Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP2Amps.setStatus("current")
if mibBuilder.loadTexts:
    meterP2Amps.setUnits("Amps")
_MeterP3Amps_Type = Unsigned32
_MeterP3Amps_Object = MibScalar
meterP3Amps = _MeterP3Amps_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7690),
    _MeterP3Amps_Type()
)
meterP3Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP3Amps.setStatus("current")
if mibBuilder.loadTexts:
    meterP3Amps.setUnits("Amps")
_MeterP1Volts_Type = Unsigned32
_MeterP1Volts_Object = MibScalar
meterP1Volts = _MeterP1Volts_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7691),
    _MeterP1Volts_Type()
)
meterP1Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP1Volts.setStatus("current")
if mibBuilder.loadTexts:
    meterP1Volts.setUnits("Voltsx10")
_MeterP2Volts_Type = Unsigned32
_MeterP2Volts_Object = MibScalar
meterP2Volts = _MeterP2Volts_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7692),
    _MeterP2Volts_Type()
)
meterP2Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP2Volts.setStatus("current")
if mibBuilder.loadTexts:
    meterP2Volts.setUnits("Voltsx10")
_MeterP3Volts_Type = Unsigned32
_MeterP3Volts_Object = MibScalar
meterP3Volts = _MeterP3Volts_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7693),
    _MeterP3Volts_Type()
)
meterP3Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP3Volts.setStatus("current")
if mibBuilder.loadTexts:
    meterP3Volts.setUnits("Voltsx10")
_MeterP1P2Volts_Type = Unsigned32
_MeterP1P2Volts_Object = MibScalar
meterP1P2Volts = _MeterP1P2Volts_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7694),
    _MeterP1P2Volts_Type()
)
meterP1P2Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP1P2Volts.setStatus("current")
if mibBuilder.loadTexts:
    meterP1P2Volts.setUnits("Voltsx10")
_MeterP2P3Volts_Type = Unsigned32
_MeterP2P3Volts_Object = MibScalar
meterP2P3Volts = _MeterP2P3Volts_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7695),
    _MeterP2P3Volts_Type()
)
meterP2P3Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP2P3Volts.setStatus("current")
if mibBuilder.loadTexts:
    meterP2P3Volts.setUnits("Voltsx10")
_MeterP3P1Volts_Type = Unsigned32
_MeterP3P1Volts_Object = MibScalar
meterP3P1Volts = _MeterP3P1Volts_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7696),
    _MeterP3P1Volts_Type()
)
meterP3P1Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP3P1Volts.setStatus("current")
if mibBuilder.loadTexts:
    meterP3P1Volts.setUnits("Voltsx10")
_MeterFreq_Type = Unsigned32
_MeterFreq_Object = MibScalar
meterFreq = _MeterFreq_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7697),
    _MeterFreq_Type()
)
meterFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterFreq.setStatus("current")
if mibBuilder.loadTexts:
    meterFreq.setUnits("Hz x 10")
_MeterPh1PF_Type = Integer32
_MeterPh1PF_Object = MibScalar
meterPh1PF = _MeterPh1PF_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7698),
    _MeterPh1PF_Type()
)
meterPh1PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPh1PF.setStatus("current")
if mibBuilder.loadTexts:
    meterPh1PF.setUnits("PF x 100")
_MeterPh2PF_Type = Integer32
_MeterPh2PF_Object = MibScalar
meterPh2PF = _MeterPh2PF_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7699),
    _MeterPh2PF_Type()
)
meterPh2PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPh2PF.setStatus("current")
if mibBuilder.loadTexts:
    meterPh2PF.setUnits("PF x 100")
_MeterPh3PF_Type = Integer32
_MeterPh3PF_Object = MibScalar
meterPh3PF = _MeterPh3PF_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7700),
    _MeterPh3PF_Type()
)
meterPh3PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPh3PF.setStatus("current")
if mibBuilder.loadTexts:
    meterPh3PF.setUnits("PF x 100")
_MeterSysPh1PF_Type = Integer32
_MeterSysPh1PF_Object = MibScalar
meterSysPh1PF = _MeterSysPh1PF_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7701),
    _MeterSysPh1PF_Type()
)
meterSysPh1PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterSysPh1PF.setStatus("current")
if mibBuilder.loadTexts:
    meterSysPh1PF.setUnits("PF x 100")
_MeterP1kW_Type = Integer32
_MeterP1kW_Object = MibScalar
meterP1kW = _MeterP1kW_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7702),
    _MeterP1kW_Type()
)
meterP1kW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP1kW.setStatus("current")
if mibBuilder.loadTexts:
    meterP1kW.setUnits("kW")
_MeterP2kW_Type = Integer32
_MeterP2kW_Object = MibScalar
meterP2kW = _MeterP2kW_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7703),
    _MeterP2kW_Type()
)
meterP2kW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP2kW.setStatus("current")
if mibBuilder.loadTexts:
    meterP2kW.setUnits("kW")
_MeterP3kW_Type = Integer32
_MeterP3kW_Object = MibScalar
meterP3kW = _MeterP3kW_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7704),
    _MeterP3kW_Type()
)
meterP3kW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP3kW.setStatus("current")
if mibBuilder.loadTexts:
    meterP3kW.setUnits("kW")
_MeterSyskW_Type = Integer32
_MeterSyskW_Object = MibScalar
meterSyskW = _MeterSyskW_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7705),
    _MeterSyskW_Type()
)
meterSyskW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterSyskW.setStatus("current")
if mibBuilder.loadTexts:
    meterSyskW.setUnits("kW")
_MeterP1kVA_Type = Unsigned32
_MeterP1kVA_Object = MibScalar
meterP1kVA = _MeterP1kVA_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7706),
    _MeterP1kVA_Type()
)
meterP1kVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP1kVA.setStatus("current")
if mibBuilder.loadTexts:
    meterP1kVA.setUnits("kVA")
_MeterP2kVA_Type = Unsigned32
_MeterP2kVA_Object = MibScalar
meterP2kVA = _MeterP2kVA_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7707),
    _MeterP2kVA_Type()
)
meterP2kVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP2kVA.setStatus("current")
if mibBuilder.loadTexts:
    meterP2kVA.setUnits("kVA")
_MeterP3kVA_Type = Unsigned32
_MeterP3kVA_Object = MibScalar
meterP3kVA = _MeterP3kVA_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7708),
    _MeterP3kVA_Type()
)
meterP3kVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP3kVA.setStatus("current")
if mibBuilder.loadTexts:
    meterP3kVA.setUnits("kVA")
_MeterSyskVA_Type = Unsigned32
_MeterSyskVA_Object = MibScalar
meterSyskVA = _MeterSyskVA_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7709),
    _MeterSyskVA_Type()
)
meterSyskVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterSyskVA.setStatus("current")
if mibBuilder.loadTexts:
    meterSyskVA.setUnits("kVA")
_MeterP1kvar_Type = Integer32
_MeterP1kvar_Object = MibScalar
meterP1kvar = _MeterP1kvar_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7710),
    _MeterP1kvar_Type()
)
meterP1kvar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP1kvar.setStatus("current")
if mibBuilder.loadTexts:
    meterP1kvar.setUnits("kvar")
_MeterP2kvar_Type = Integer32
_MeterP2kvar_Object = MibScalar
meterP2kvar = _MeterP2kvar_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7711),
    _MeterP2kvar_Type()
)
meterP2kvar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP2kvar.setStatus("current")
if mibBuilder.loadTexts:
    meterP2kvar.setUnits("kvar")
_MeterP3kvar_Type = Integer32
_MeterP3kvar_Object = MibScalar
meterP3kvar = _MeterP3kvar_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7712),
    _MeterP3kvar_Type()
)
meterP3kvar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP3kvar.setStatus("current")
if mibBuilder.loadTexts:
    meterP3kvar.setUnits("kvar")
_MeterSyskvar_Type = Integer32
_MeterSyskvar_Object = MibScalar
meterSyskvar = _MeterSyskvar_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7713),
    _MeterSyskvar_Type()
)
meterSyskvar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterSyskvar.setStatus("current")
if mibBuilder.loadTexts:
    meterSyskvar.setUnits("kvar")
_MeterP1AmpsDem_Type = Unsigned32
_MeterP1AmpsDem_Object = MibScalar
meterP1AmpsDem = _MeterP1AmpsDem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7714),
    _MeterP1AmpsDem_Type()
)
meterP1AmpsDem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP1AmpsDem.setStatus("current")
if mibBuilder.loadTexts:
    meterP1AmpsDem.setUnits("Amps")
_MeterP2AmpsDem_Type = Unsigned32
_MeterP2AmpsDem_Object = MibScalar
meterP2AmpsDem = _MeterP2AmpsDem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7715),
    _MeterP2AmpsDem_Type()
)
meterP2AmpsDem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP2AmpsDem.setStatus("current")
if mibBuilder.loadTexts:
    meterP2AmpsDem.setUnits("Amps")
_MeterP3AmpsDem_Type = Unsigned32
_MeterP3AmpsDem_Object = MibScalar
meterP3AmpsDem = _MeterP3AmpsDem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7716),
    _MeterP3AmpsDem_Type()
)
meterP3AmpsDem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP3AmpsDem.setStatus("current")
if mibBuilder.loadTexts:
    meterP3AmpsDem.setUnits("Amps")
_MeterP1VoltsDem_Type = Unsigned32
_MeterP1VoltsDem_Object = MibScalar
meterP1VoltsDem = _MeterP1VoltsDem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7717),
    _MeterP1VoltsDem_Type()
)
meterP1VoltsDem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP1VoltsDem.setStatus("current")
if mibBuilder.loadTexts:
    meterP1VoltsDem.setUnits("Voltsx10")
_MeterP2VoltsDem_Type = Unsigned32
_MeterP2VoltsDem_Object = MibScalar
meterP2VoltsDem = _MeterP2VoltsDem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7718),
    _MeterP2VoltsDem_Type()
)
meterP2VoltsDem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP2VoltsDem.setStatus("current")
if mibBuilder.loadTexts:
    meterP2VoltsDem.setUnits("Voltsx10")
_MeterP3VoltsDem_Type = Unsigned32
_MeterP3VoltsDem_Object = MibScalar
meterP3VoltsDem = _MeterP3VoltsDem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7719),
    _MeterP3VoltsDem_Type()
)
meterP3VoltsDem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterP3VoltsDem.setStatus("current")
if mibBuilder.loadTexts:
    meterP3VoltsDem.setUnits("Voltsx10")
_MeterPkP1Amps_Type = Unsigned32
_MeterPkP1Amps_Object = MibScalar
meterPkP1Amps = _MeterPkP1Amps_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7720),
    _MeterPkP1Amps_Type()
)
meterPkP1Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPkP1Amps.setStatus("current")
if mibBuilder.loadTexts:
    meterPkP1Amps.setUnits("Amps")
_MeterPkP2Amps_Type = Unsigned32
_MeterPkP2Amps_Object = MibScalar
meterPkP2Amps = _MeterPkP2Amps_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7721),
    _MeterPkP2Amps_Type()
)
meterPkP2Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPkP2Amps.setStatus("current")
if mibBuilder.loadTexts:
    meterPkP2Amps.setUnits("Amps")
_MeterPkP3Amps_Type = Unsigned32
_MeterPkP3Amps_Object = MibScalar
meterPkP3Amps = _MeterPkP3Amps_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7722),
    _MeterPkP3Amps_Type()
)
meterPkP3Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPkP3Amps.setStatus("current")
if mibBuilder.loadTexts:
    meterPkP3Amps.setUnits("Amps")
_MeterPkP1Volts_Type = Unsigned32
_MeterPkP1Volts_Object = MibScalar
meterPkP1Volts = _MeterPkP1Volts_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7723),
    _MeterPkP1Volts_Type()
)
meterPkP1Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPkP1Volts.setStatus("current")
if mibBuilder.loadTexts:
    meterPkP1Volts.setUnits("Voltsx10")
_MeterPkP2Volts_Type = Unsigned32
_MeterPkP2Volts_Object = MibScalar
meterPkP2Volts = _MeterPkP2Volts_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7724),
    _MeterPkP2Volts_Type()
)
meterPkP2Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPkP2Volts.setStatus("current")
if mibBuilder.loadTexts:
    meterPkP2Volts.setUnits("Voltsx10")
_MeterPkP3Volts_Type = Unsigned32
_MeterPkP3Volts_Object = MibScalar
meterPkP3Volts = _MeterPkP3Volts_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7725),
    _MeterPkP3Volts_Type()
)
meterPkP3Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPkP3Volts.setStatus("current")
if mibBuilder.loadTexts:
    meterPkP3Volts.setUnits("Voltsx10")
_MeterkWDem_Type = Integer32
_MeterkWDem_Object = MibScalar
meterkWDem = _MeterkWDem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7726),
    _MeterkWDem_Type()
)
meterkWDem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterkWDem.setStatus("current")
if mibBuilder.loadTexts:
    meterkWDem.setUnits("kW")
_MeterkVADem_Type = Unsigned32
_MeterkVADem_Object = MibScalar
meterkVADem = _MeterkVADem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7727),
    _MeterkVADem_Type()
)
meterkVADem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterkVADem.setStatus("current")
if mibBuilder.loadTexts:
    meterkVADem.setUnits("kVA")
_MeterkvarDem_Type = Integer32
_MeterkvarDem_Object = MibScalar
meterkvarDem = _MeterkvarDem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7728),
    _MeterkvarDem_Type()
)
meterkvarDem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterkvarDem.setStatus("current")
if mibBuilder.loadTexts:
    meterkvarDem.setUnits("kvar")
_MeterPkkWDem_Type = Integer32
_MeterPkkWDem_Object = MibScalar
meterPkkWDem = _MeterPkkWDem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7729),
    _MeterPkkWDem_Type()
)
meterPkkWDem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPkkWDem.setStatus("current")
if mibBuilder.loadTexts:
    meterPkkWDem.setUnits("kW")
_MeterPkkVADem_Type = Unsigned32
_MeterPkkVADem_Object = MibScalar
meterPkkVADem = _MeterPkkVADem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7730),
    _MeterPkkVADem_Type()
)
meterPkkVADem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPkkVADem.setStatus("current")
if mibBuilder.loadTexts:
    meterPkkVADem.setUnits("kVA")
_MeterPkkvarDem_Type = Integer32
_MeterPkkvarDem_Object = MibScalar
meterPkkvarDem = _MeterPkkvarDem_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7731),
    _MeterPkkvarDem_Type()
)
meterPkkvarDem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPkkvarDem.setStatus("current")
if mibBuilder.loadTexts:
    meterPkkvarDem.setUnits("kvar")
_MeterNeuAmps_Type = Unsigned32
_MeterNeuAmps_Object = MibScalar
meterNeuAmps = _MeterNeuAmps_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7732),
    _MeterNeuAmps_Type()
)
meterNeuAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterNeuAmps.setStatus("current")
if mibBuilder.loadTexts:
    meterNeuAmps.setUnits("Amps")
_MeterAmpsScal_Type = Unsigned32
_MeterAmpsScal_Object = MibScalar
meterAmpsScal = _MeterAmpsScal_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7733),
    _MeterAmpsScal_Type()
)
meterAmpsScal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterAmpsScal.setStatus("current")
if mibBuilder.loadTexts:
    meterAmpsScal.setUnits("Ki")
_MeterPhVoltScal_Type = Unsigned32
_MeterPhVoltScal_Object = MibScalar
meterPhVoltScal = _MeterPhVoltScal_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7734),
    _MeterPhVoltScal_Type()
)
meterPhVoltScal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPhVoltScal.setStatus("current")
if mibBuilder.loadTexts:
    meterPhVoltScal.setUnits("Kvp")
_MeterLLVoltScal_Type = Unsigned32
_MeterLLVoltScal_Object = MibScalar
meterLLVoltScal = _MeterLLVoltScal_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7735),
    _MeterLLVoltScal_Type()
)
meterLLVoltScal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterLLVoltScal.setStatus("current")
if mibBuilder.loadTexts:
    meterLLVoltScal.setUnits("Kvl")
_MeterPowerScal_Type = Unsigned32
_MeterPowerScal_Object = MibScalar
meterPowerScal = _MeterPowerScal_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7736),
    _MeterPowerScal_Type()
)
meterPowerScal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterPowerScal.setStatus("current")
if mibBuilder.loadTexts:
    meterPowerScal.setUnits("Kp")
_MeterEnergyScal_Type = Unsigned32
_MeterEnergyScal_Object = MibScalar
meterEnergyScal = _MeterEnergyScal_Object(
    (1, 3, 6, 1, 4, 1, 37778, 7737),
    _MeterEnergyScal_Type()
)
meterEnergyScal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterEnergyScal.setStatus("current")
if mibBuilder.loadTexts:
    meterEnergyScal.setUnits("Ke")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ND020-MIB",
    **{"ndMeter": ndMeter,
       "meterkWhH": meterkWhH,
       "meterkWhL": meterkWhL,
       "meterkVAhH": meterkVAhH,
       "meterkVAhL": meterkVAhL,
       "meterkvarhH": meterkvarhH,
       "meterkvarhL": meterkvarhL,
       "meterEkWhH": meterEkWhH,
       "meterEkWhL": meterEkWhL,
       "meterP1Amps": meterP1Amps,
       "meterP2Amps": meterP2Amps,
       "meterP3Amps": meterP3Amps,
       "meterP1Volts": meterP1Volts,
       "meterP2Volts": meterP2Volts,
       "meterP3Volts": meterP3Volts,
       "meterP1P2Volts": meterP1P2Volts,
       "meterP2P3Volts": meterP2P3Volts,
       "meterP3P1Volts": meterP3P1Volts,
       "meterFreq": meterFreq,
       "meterPh1PF": meterPh1PF,
       "meterPh2PF": meterPh2PF,
       "meterPh3PF": meterPh3PF,
       "meterSysPh1PF": meterSysPh1PF,
       "meterP1kW": meterP1kW,
       "meterP2kW": meterP2kW,
       "meterP3kW": meterP3kW,
       "meterSyskW": meterSyskW,
       "meterP1kVA": meterP1kVA,
       "meterP2kVA": meterP2kVA,
       "meterP3kVA": meterP3kVA,
       "meterSyskVA": meterSyskVA,
       "meterP1kvar": meterP1kvar,
       "meterP2kvar": meterP2kvar,
       "meterP3kvar": meterP3kvar,
       "meterSyskvar": meterSyskvar,
       "meterP1AmpsDem": meterP1AmpsDem,
       "meterP2AmpsDem": meterP2AmpsDem,
       "meterP3AmpsDem": meterP3AmpsDem,
       "meterP1VoltsDem": meterP1VoltsDem,
       "meterP2VoltsDem": meterP2VoltsDem,
       "meterP3VoltsDem": meterP3VoltsDem,
       "meterPkP1Amps": meterPkP1Amps,
       "meterPkP2Amps": meterPkP2Amps,
       "meterPkP3Amps": meterPkP3Amps,
       "meterPkP1Volts": meterPkP1Volts,
       "meterPkP2Volts": meterPkP2Volts,
       "meterPkP3Volts": meterPkP3Volts,
       "meterkWDem": meterkWDem,
       "meterkVADem": meterkVADem,
       "meterkvarDem": meterkvarDem,
       "meterPkkWDem": meterPkkWDem,
       "meterPkkVADem": meterPkkVADem,
       "meterPkkvarDem": meterPkkvarDem,
       "meterNeuAmps": meterNeuAmps,
       "meterAmpsScal": meterAmpsScal,
       "meterPhVoltScal": meterPhVoltScal,
       "meterLLVoltScal": meterLLVoltScal,
       "meterPowerScal": meterPowerScal,
       "meterEnergyScal": meterEnergyScal}
)
