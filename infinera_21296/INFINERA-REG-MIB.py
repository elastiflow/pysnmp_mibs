# SNMP MIB module (INFINERA-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/infinera_21296/INFINERA-REG-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:49:16 2025
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
 iso,
 org) = mibBuilder.importSymbols(
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
    "iso",
    "org")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

infinera = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296)
)
if mibBuilder.loadTexts:
    infinera.setRevisions(
        ("2008-09-05 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Don_ObjectIdentity = ObjectIdentity
don = _Don_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2)
)
if mibBuilder.loadTexts:
    don.setStatus("current")
_Base_ObjectIdentity = ObjectIdentity
base = _Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 1)
)
if mibBuilder.loadTexts:
    base.setStatus("current")
_Ne_ObjectIdentity = ObjectIdentity
ne = _Ne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2)
)
if mibBuilder.loadTexts:
    ne.setStatus("current")
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1)
)
_InfnNE_ObjectIdentity = ObjectIdentity
infnNE = _InfnNE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8)
)
_CommonEquipment_ObjectIdentity = ObjectIdentity
commonEquipment = _CommonEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9)
)
_CommonTerminationPoint_ObjectIdentity = ObjectIdentity
commonTerminationPoint = _CommonTerminationPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10)
)
_CommonPerfMon_ObjectIdentity = ObjectIdentity
commonPerfMon = _CommonPerfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11)
)
_Dtn_ObjectIdentity = ObjectIdentity
dtn = _Dtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2)
)
_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1)
)
_TerminationPoint_ObjectIdentity = ObjectIdentity
terminationPoint = _TerminationPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2)
)
_PerfMon_ObjectIdentity = ObjectIdentity
perfMon = _PerfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3)
)
_Ola_ObjectIdentity = ObjectIdentity
ola = _Ola_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 3)
)
_Ems_ObjectIdentity = ObjectIdentity
ems = _Ems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 3)
)
if mibBuilder.loadTexts:
    ems.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-REG-MIB",
    **{"dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "infinera": infinera,
       "don": don,
       "base": base,
       "ne": ne,
       "common": common,
       "infnNE": infnNE,
       "commonEquipment": commonEquipment,
       "commonTerminationPoint": commonTerminationPoint,
       "commonPerfMon": commonPerfMon,
       "dtn": dtn,
       "equipment": equipment,
       "terminationPoint": terminationPoint,
       "perfMon": perfMon,
       "ola": ola,
       "ems": ems}
)
