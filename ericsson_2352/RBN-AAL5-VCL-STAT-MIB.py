# SNMP MIB module (RBN-AAL5-VCL-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-AAL5-VCL-STAT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:57 2025
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(rbnXAtmAal5VclStatEntry,) = mibBuilder.importSymbols(
    "RBN-X-AAL5-VCL-STAT-MIB",
    "rbnXAtmAal5VclStatEntry")

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

rbnAal5VclStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 1)
)
if mibBuilder.loadTexts:
    rbnAal5VclStatMIB.setRevisions(
        ("2011-01-19 18:00",
         "2002-05-29 00:00",
         "1998-04-17 16:45")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnAal5VclStatMIBObjects_ObjectIdentity = ObjectIdentity
rbnAal5VclStatMIBObjects = _RbnAal5VclStatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 1, 1)
)
_RbnAtmAal5VclStatTable_Object = MibTable
rbnAtmAal5VclStatTable = _RbnAtmAal5VclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtmAal5VclStatTable.setStatus("current")
_RbnAtmAal5VclStatEntry_Object = MibTableRow
rbnAtmAal5VclStatEntry = _RbnAtmAal5VclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtmAal5VclStatEntry.setStatus("current")
_RbnAtmAal5VclOutDrops_Type = Counter32
_RbnAtmAal5VclOutDrops_Object = MibTableColumn
rbnAtmAal5VclOutDrops = _RbnAtmAal5VclOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 1, 1, 1, 1, 1),
    _RbnAtmAal5VclOutDrops_Type()
)
rbnAtmAal5VclOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAtmAal5VclOutDrops.setStatus("current")
_RbnAal5VclStatMIBConformance_ObjectIdentity = ObjectIdentity
rbnAal5VclStatMIBConformance = _RbnAal5VclStatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 1, 2)
)
_RbnAal5VclStatMIBGroups_ObjectIdentity = ObjectIdentity
rbnAal5VclStatMIBGroups = _RbnAal5VclStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 1)
)
_RbnAal5VclStatMIBCompliances_ObjectIdentity = ObjectIdentity
rbnAal5VclStatMIBCompliances = _RbnAal5VclStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 2)
)
rbnXAtmAal5VclStatEntry.registerAugmentions(
    ("RBN-AAL5-VCL-STAT-MIB",
     "rbnAtmAal5VclStatEntry")
)
rbnAtmAal5VclStatEntry.setIndexNames(*rbnXAtmAal5VclStatEntry.getIndexNames())

# Managed Objects groups

rbnAal5VclStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 1, 1)
)
rbnAal5VclStatGroup.setObjects(
    ("RBN-AAL5-VCL-STAT-MIB", "rbnAtmAal5VclOutDrops")
)
if mibBuilder.loadTexts:
    rbnAal5VclStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnAal5VclStatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 2, 1)
)
rbnAal5VclStatMIBCompliance.setObjects(
    ("RBN-AAL5-VCL-STAT-MIB", "rbnAal5VclStatGroup")
)
if mibBuilder.loadTexts:
    rbnAal5VclStatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-AAL5-VCL-STAT-MIB",
    **{"rbnAal5VclStatMIB": rbnAal5VclStatMIB,
       "rbnAal5VclStatMIBObjects": rbnAal5VclStatMIBObjects,
       "rbnAtmAal5VclStatTable": rbnAtmAal5VclStatTable,
       "rbnAtmAal5VclStatEntry": rbnAtmAal5VclStatEntry,
       "rbnAtmAal5VclOutDrops": rbnAtmAal5VclOutDrops,
       "rbnAal5VclStatMIBConformance": rbnAal5VclStatMIBConformance,
       "rbnAal5VclStatMIBGroups": rbnAal5VclStatMIBGroups,
       "rbnAal5VclStatGroup": rbnAal5VclStatGroup,
       "rbnAal5VclStatMIBCompliances": rbnAal5VclStatMIBCompliances,
       "rbnAal5VclStatMIBCompliance": rbnAal5VclStatMIBCompliance}
)
