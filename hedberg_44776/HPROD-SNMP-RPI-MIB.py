# SNMP MIB module (HPROD-SNMP-RPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hedberg_44776/HPROD-SNMP-RPI-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:32:02 2025
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

(hPsnmpMIBS,
 hPsnmpMIBgroups,
 hPsnmpModuleCompliances,
 hPsnmpModuleIdentity) = mibBuilder.importSymbols(
    "HPROD-SNMP-MIB",
    "hPsnmpMIBS",
    "hPsnmpMIBgroups",
    "hPsnmpModuleCompliances",
    "hPsnmpModuleIdentity")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hPsnmpRpiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44776, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hPsnmpRpiMIB.setRevisions(
        ("2015-03-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HPsnmpRpiRoot_ObjectIdentity = ObjectIdentity
hPsnmpRpiRoot = _HPsnmpRpiRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44776, 1, 3, 1)
)
_HPsnmpRpiCpuTemp_Type = Gauge32
_HPsnmpRpiCpuTemp_Object = MibScalar
hPsnmpRpiCpuTemp = _HPsnmpRpiCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 44776, 1, 3, 1, 1),
    _HPsnmpRpiCpuTemp_Type()
)
hPsnmpRpiCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hPsnmpRpiCpuTemp.setStatus("current")

# Managed Objects groups

hPsnmpGroupRpi = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44776, 1, 1, 1)
)
hPsnmpGroupRpi.setObjects(
    ("HPROD-SNMP-RPI-MIB", "hPsnmpRpiCpuTemp")
)
if mibBuilder.loadTexts:
    hPsnmpGroupRpi.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hPsnmpRpiMIBcompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44776, 1, 4, 2)
)
hPsnmpRpiMIBcompliance.setObjects(
    ("HPROD-SNMP-RPI-MIB", "hPsnmpGroupRpi")
)
if mibBuilder.loadTexts:
    hPsnmpRpiMIBcompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPROD-SNMP-RPI-MIB",
    **{"hPsnmpGroupRpi": hPsnmpGroupRpi,
       "hPsnmpRpiMIB": hPsnmpRpiMIB,
       "hPsnmpRpiRoot": hPsnmpRpiRoot,
       "hPsnmpRpiCpuTemp": hPsnmpRpiCpuTemp,
       "hPsnmpRpiMIBcompliance": hPsnmpRpiMIBcompliance}
)
