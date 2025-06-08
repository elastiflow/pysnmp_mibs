# SNMP MIB module (ARISTA-TAPAGG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-TAPAGG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(AristaQosShortId,) = mibBuilder.importSymbols(
    "ARISTA-QOS-MIB",
    "AristaQosShortId")

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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

aristaTapaggMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31)
)
if mibBuilder.loadTexts:
    aristaTapaggMIB.setRevisions(
        ("2021-04-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaTapaggMibObjects_ObjectIdentity = ObjectIdentity
aristaTapaggMibObjects = _AristaTapaggMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1)
)
_AristaTapaggPolicyTable_Object = MibTable
aristaTapaggPolicyTable = _AristaTapaggPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1, 1)
)
if mibBuilder.loadTexts:
    aristaTapaggPolicyTable.setStatus("current")
_AristaTapaggPolicyEntry_Object = MibTableRow
aristaTapaggPolicyEntry = _AristaTapaggPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1, 1, 1)
)
aristaTapaggPolicyEntry.setIndexNames(
    (0, "ARISTA-TAPAGG-MIB", "aristaTapaggPolicyId"),
)
if mibBuilder.loadTexts:
    aristaTapaggPolicyEntry.setStatus("current")
_AristaTapaggPolicyId_Type = AristaQosShortId
_AristaTapaggPolicyId_Object = MibTableColumn
aristaTapaggPolicyId = _AristaTapaggPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1, 1, 1, 1),
    _AristaTapaggPolicyId_Type()
)
aristaTapaggPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaTapaggPolicyId.setStatus("current")


class _AristaTapaggPolicyName_Type(DisplayString):
    """Custom type aristaTapaggPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AristaTapaggPolicyName_Type.__name__ = "DisplayString"
_AristaTapaggPolicyName_Object = MibTableColumn
aristaTapaggPolicyName = _AristaTapaggPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1, 1, 1, 2),
    _AristaTapaggPolicyName_Type()
)
aristaTapaggPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaTapaggPolicyName.setStatus("current")
_AristaTapaggPolicyClassTable_Object = MibTable
aristaTapaggPolicyClassTable = _AristaTapaggPolicyClassTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1, 2)
)
if mibBuilder.loadTexts:
    aristaTapaggPolicyClassTable.setStatus("current")
_AristaTapaggPolicyClassEntry_Object = MibTableRow
aristaTapaggPolicyClassEntry = _AristaTapaggPolicyClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1, 2, 1)
)
aristaTapaggPolicyClassEntry.setIndexNames(
    (0, "ARISTA-TAPAGG-MIB", "aristaTapaggPolicyId"),
    (0, "ARISTA-TAPAGG-MIB", "aristaTapaggPolicyClassIndex"),
)
if mibBuilder.loadTexts:
    aristaTapaggPolicyClassEntry.setStatus("current")


class _AristaTapaggPolicyClassIndex_Type(Integer32):
    """Custom type aristaTapaggPolicyClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AristaTapaggPolicyClassIndex_Type.__name__ = "Integer32"
_AristaTapaggPolicyClassIndex_Object = MibTableColumn
aristaTapaggPolicyClassIndex = _AristaTapaggPolicyClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1, 2, 1, 1),
    _AristaTapaggPolicyClassIndex_Type()
)
aristaTapaggPolicyClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaTapaggPolicyClassIndex.setStatus("current")


class _AristaTapaggPolicyClassName_Type(DisplayString):
    """Custom type aristaTapaggPolicyClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AristaTapaggPolicyClassName_Type.__name__ = "DisplayString"
_AristaTapaggPolicyClassName_Object = MibTableColumn
aristaTapaggPolicyClassName = _AristaTapaggPolicyClassName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1, 2, 1, 2),
    _AristaTapaggPolicyClassName_Type()
)
aristaTapaggPolicyClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaTapaggPolicyClassName.setStatus("current")
_AristaTapaggPolicyPktsMatched_Type = Counter64
_AristaTapaggPolicyPktsMatched_Object = MibTableColumn
aristaTapaggPolicyPktsMatched = _AristaTapaggPolicyPktsMatched_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1, 2, 1, 3),
    _AristaTapaggPolicyPktsMatched_Type()
)
aristaTapaggPolicyPktsMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaTapaggPolicyPktsMatched.setStatus("current")
_AristaTapaggPolicyBytesMatched_Type = Counter64
_AristaTapaggPolicyBytesMatched_Object = MibTableColumn
aristaTapaggPolicyBytesMatched = _AristaTapaggPolicyBytesMatched_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 1, 2, 1, 4),
    _AristaTapaggPolicyBytesMatched_Type()
)
aristaTapaggPolicyBytesMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaTapaggPolicyBytesMatched.setStatus("current")
_AristaTapaggMibConformance_ObjectIdentity = ObjectIdentity
aristaTapaggMibConformance = _AristaTapaggMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 2)
)
_AristaTapaggMibCompliances_ObjectIdentity = ObjectIdentity
aristaTapaggMibCompliances = _AristaTapaggMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 2, 1)
)
_AristaTapaggMibGroups_ObjectIdentity = ObjectIdentity
aristaTapaggMibGroups = _AristaTapaggMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 2, 2)
)

# Managed Objects groups

aristaTapaggPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 2, 2, 1)
)
aristaTapaggPolicyGroup.setObjects(
      *(("ARISTA-TAPAGG-MIB", "aristaTapaggPolicyName"),
        ("ARISTA-TAPAGG-MIB", "aristaTapaggPolicyClassName"),
        ("ARISTA-TAPAGG-MIB", "aristaTapaggPolicyPktsMatched"),
        ("ARISTA-TAPAGG-MIB", "aristaTapaggPolicyBytesMatched"))
)
if mibBuilder.loadTexts:
    aristaTapaggPolicyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaTapaggMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 31, 2, 1, 1)
)
aristaTapaggMibCompliance.setObjects(
    ("ARISTA-TAPAGG-MIB", "aristaTapaggPolicyGroup")
)
if mibBuilder.loadTexts:
    aristaTapaggMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-TAPAGG-MIB",
    **{"aristaTapaggMIB": aristaTapaggMIB,
       "aristaTapaggMibObjects": aristaTapaggMibObjects,
       "aristaTapaggPolicyTable": aristaTapaggPolicyTable,
       "aristaTapaggPolicyEntry": aristaTapaggPolicyEntry,
       "aristaTapaggPolicyId": aristaTapaggPolicyId,
       "aristaTapaggPolicyName": aristaTapaggPolicyName,
       "aristaTapaggPolicyClassTable": aristaTapaggPolicyClassTable,
       "aristaTapaggPolicyClassEntry": aristaTapaggPolicyClassEntry,
       "aristaTapaggPolicyClassIndex": aristaTapaggPolicyClassIndex,
       "aristaTapaggPolicyClassName": aristaTapaggPolicyClassName,
       "aristaTapaggPolicyPktsMatched": aristaTapaggPolicyPktsMatched,
       "aristaTapaggPolicyBytesMatched": aristaTapaggPolicyBytesMatched,
       "aristaTapaggMibConformance": aristaTapaggMibConformance,
       "aristaTapaggMibCompliances": aristaTapaggMibCompliances,
       "aristaTapaggMibCompliance": aristaTapaggMibCompliance,
       "aristaTapaggMibGroups": aristaTapaggMibGroups,
       "aristaTapaggPolicyGroup": aristaTapaggPolicyGroup}
)
