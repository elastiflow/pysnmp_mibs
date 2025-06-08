# SNMP MIB module (RBN-X-AAL5-VCL-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-X-AAL5-VCL-STAT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:27 2025
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

(atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(rbnExperiment,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnExperiment")

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

rbnXAal5VclStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1)
)
if mibBuilder.loadTexts:
    rbnXAal5VclStatMIB.setRevisions(
        ("2011-01-19 18:00",
         "1998-04-17 16:45")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnXAal5VclStatMIBObjects_ObjectIdentity = ObjectIdentity
rbnXAal5VclStatMIBObjects = _RbnXAal5VclStatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 1)
)
_RbnXAtmAal5VclStatTable_Object = MibTable
rbnXAtmAal5VclStatTable = _RbnXAtmAal5VclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnXAtmAal5VclStatTable.setStatus("deprecated")
_RbnXAtmAal5VclStatEntry_Object = MibTableRow
rbnXAtmAal5VclStatEntry = _RbnXAtmAal5VclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1)
)
rbnXAtmAal5VclStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    rbnXAtmAal5VclStatEntry.setStatus("deprecated")
_RbnXAtmAal5VclInPkts_Type = Counter32
_RbnXAtmAal5VclInPkts_Object = MibTableColumn
rbnXAtmAal5VclInPkts = _RbnXAtmAal5VclInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 1),
    _RbnXAtmAal5VclInPkts_Type()
)
rbnXAtmAal5VclInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnXAtmAal5VclInPkts.setStatus("deprecated")
_RbnXAtmAal5VclOutPkts_Type = Counter32
_RbnXAtmAal5VclOutPkts_Object = MibTableColumn
rbnXAtmAal5VclOutPkts = _RbnXAtmAal5VclOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 2),
    _RbnXAtmAal5VclOutPkts_Type()
)
rbnXAtmAal5VclOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnXAtmAal5VclOutPkts.setStatus("deprecated")
_RbnXAtmAal5VclInOctets_Type = Counter32
_RbnXAtmAal5VclInOctets_Object = MibTableColumn
rbnXAtmAal5VclInOctets = _RbnXAtmAal5VclInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 3),
    _RbnXAtmAal5VclInOctets_Type()
)
rbnXAtmAal5VclInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnXAtmAal5VclInOctets.setStatus("deprecated")
_RbnXAtmAal5VclOutOctets_Type = Counter32
_RbnXAtmAal5VclOutOctets_Object = MibTableColumn
rbnXAtmAal5VclOutOctets = _RbnXAtmAal5VclOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 4),
    _RbnXAtmAal5VclOutOctets_Type()
)
rbnXAtmAal5VclOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnXAtmAal5VclOutOctets.setStatus("deprecated")
_RbnXAal5VclStatMIBConformance_ObjectIdentity = ObjectIdentity
rbnXAal5VclStatMIBConformance = _RbnXAal5VclStatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 2)
)
_RbnXAal5VclStatMIBGroups_ObjectIdentity = ObjectIdentity
rbnXAal5VclStatMIBGroups = _RbnXAal5VclStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 1)
)
_RbnXAal5VclStatMIBCompliances_ObjectIdentity = ObjectIdentity
rbnXAal5VclStatMIBCompliances = _RbnXAal5VclStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 2)
)

# Managed Objects groups

rbnXAal5VclStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 1, 1)
)
rbnXAal5VclStatGroup.setObjects(
      *(("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclInPkts"),
        ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclOutPkts"),
        ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclInOctets"),
        ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclOutOctets"))
)
if mibBuilder.loadTexts:
    rbnXAal5VclStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnXAal5VclStatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 2, 1)
)
rbnXAal5VclStatMIBCompliance.setObjects(
    ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAal5VclStatGroup")
)
if mibBuilder.loadTexts:
    rbnXAal5VclStatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-X-AAL5-VCL-STAT-MIB",
    **{"rbnXAal5VclStatMIB": rbnXAal5VclStatMIB,
       "rbnXAal5VclStatMIBObjects": rbnXAal5VclStatMIBObjects,
       "rbnXAtmAal5VclStatTable": rbnXAtmAal5VclStatTable,
       "rbnXAtmAal5VclStatEntry": rbnXAtmAal5VclStatEntry,
       "rbnXAtmAal5VclInPkts": rbnXAtmAal5VclInPkts,
       "rbnXAtmAal5VclOutPkts": rbnXAtmAal5VclOutPkts,
       "rbnXAtmAal5VclInOctets": rbnXAtmAal5VclInOctets,
       "rbnXAtmAal5VclOutOctets": rbnXAtmAal5VclOutOctets,
       "rbnXAal5VclStatMIBConformance": rbnXAal5VclStatMIBConformance,
       "rbnXAal5VclStatMIBGroups": rbnXAal5VclStatMIBGroups,
       "rbnXAal5VclStatGroup": rbnXAal5VclStatGroup,
       "rbnXAal5VclStatMIBCompliances": rbnXAal5VclStatMIBCompliances,
       "rbnXAal5VclStatMIBCompliance": rbnXAal5VclStatMIBCompliance}
)
