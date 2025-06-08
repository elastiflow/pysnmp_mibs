# SNMP MIB module (CHARITE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/charite_44938/CHARITE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:32:26 2025
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

chariteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44938)
)
if mibBuilder.loadTexts:
    chariteMIB.setRevisions(
        ("2016-07-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChariteMIBObjects_ObjectIdentity = ObjectIdentity
chariteMIBObjects = _ChariteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44938, 1)
)
_CharitePostfixObjects_ObjectIdentity = ObjectIdentity
charitePostfixObjects = _CharitePostfixObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44938, 1, 1)
)
_PfQueueActive_Type = Unsigned32
_PfQueueActive_Object = MibScalar
pfQueueActive = _PfQueueActive_Object(
    (1, 3, 6, 1, 4, 1, 44938, 1, 1, 1),
    _PfQueueActive_Type()
)
pfQueueActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfQueueActive.setStatus("current")
_PfQueueDeferred_Type = Unsigned32
_PfQueueDeferred_Object = MibScalar
pfQueueDeferred = _PfQueueDeferred_Object(
    (1, 3, 6, 1, 4, 1, 44938, 1, 1, 2),
    _PfQueueDeferred_Type()
)
pfQueueDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfQueueDeferred.setStatus("current")
_PfQueueHold_Type = Unsigned32
_PfQueueHold_Object = MibScalar
pfQueueHold = _PfQueueHold_Object(
    (1, 3, 6, 1, 4, 1, 44938, 1, 1, 3),
    _PfQueueHold_Type()
)
pfQueueHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfQueueHold.setStatus("current")
_PfQueueMaildrop_Type = Unsigned32
_PfQueueMaildrop_Object = MibScalar
pfQueueMaildrop = _PfQueueMaildrop_Object(
    (1, 3, 6, 1, 4, 1, 44938, 1, 1, 4),
    _PfQueueMaildrop_Type()
)
pfQueueMaildrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfQueueMaildrop.setStatus("current")
_ChariteConformance_ObjectIdentity = ObjectIdentity
chariteConformance = _ChariteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44938, 2)
)
_ChariteCompliances_ObjectIdentity = ObjectIdentity
chariteCompliances = _ChariteCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44938, 2, 1)
)
_ChariteGroups_ObjectIdentity = ObjectIdentity
chariteGroups = _ChariteGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44938, 2, 2)
)

# Managed Objects groups

postfixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44938, 2, 2, 1)
)
postfixGroup.setObjects(
      *(("CHARITE-MIB", "pfQueueActive"),
        ("CHARITE-MIB", "pfQueueDeferred"),
        ("CHARITE-MIB", "pfQueueHold"),
        ("CHARITE-MIB", "pfQueueMaildrop"))
)
if mibBuilder.loadTexts:
    postfixGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHARITE-MIB",
    **{"chariteMIB": chariteMIB,
       "chariteMIBObjects": chariteMIBObjects,
       "charitePostfixObjects": charitePostfixObjects,
       "pfQueueActive": pfQueueActive,
       "pfQueueDeferred": pfQueueDeferred,
       "pfQueueHold": pfQueueHold,
       "pfQueueMaildrop": pfQueueMaildrop,
       "chariteConformance": chariteConformance,
       "chariteCompliances": chariteCompliances,
       "chariteGroups": chariteGroups,
       "postfixGroup": postfixGroup}
)
