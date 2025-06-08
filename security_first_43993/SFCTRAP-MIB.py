# SNMP MIB module (SFCTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/security_first_43993/SFCTRAP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:57:06 2025
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

xyzCorpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43993)
)
if mibBuilder.loadTexts:
    xyzCorpMib.setRevisions(
        ("1907-10-17 22:09",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfcEventNotify_ObjectIdentity = ObjectIdentity
sfcEventNotify = _SfcEventNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43993, 3)
)
_XyzTrapsGroup_ObjectIdentity = ObjectIdentity
xyzTrapsGroup = _XyzTrapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43993, 3, 1)
)
_XyzTrapObjectsGroup_ObjectIdentity = ObjectIdentity
xyzTrapObjectsGroup = _XyzTrapObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43993, 3, 1, 1)
)
_SfcEventEntryId_Type = OctetString
_SfcEventEntryId_Object = MibScalar
sfcEventEntryId = _SfcEventEntryId_Object(
    (1, 3, 6, 1, 4, 1, 43993, 3, 1, 1, 1),
    _SfcEventEntryId_Type()
)
sfcEventEntryId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sfcEventEntryId.setStatus("current")
_SfcEventEntrySev_Type = OctetString
_SfcEventEntrySev_Object = MibScalar
sfcEventEntrySev = _SfcEventEntrySev_Object(
    (1, 3, 6, 1, 4, 1, 43993, 3, 1, 1, 2),
    _SfcEventEntrySev_Type()
)
sfcEventEntrySev.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sfcEventEntrySev.setStatus("current")
_SfcEventEntryMsg_Type = OctetString
_SfcEventEntryMsg_Object = MibScalar
sfcEventEntryMsg = _SfcEventEntryMsg_Object(
    (1, 3, 6, 1, 4, 1, 43993, 3, 1, 1, 3),
    _SfcEventEntryMsg_Type()
)
sfcEventEntryMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sfcEventEntryMsg.setStatus("current")
_SfcEventEntryType_Type = OctetString
_SfcEventEntryType_Object = MibScalar
sfcEventEntryType = _SfcEventEntryType_Object(
    (1, 3, 6, 1, 4, 1, 43993, 3, 1, 1, 4),
    _SfcEventEntryType_Type()
)
sfcEventEntryType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sfcEventEntryType.setStatus("current")
_XyzTrapDefinitionsGroup_ObjectIdentity = ObjectIdentity
xyzTrapDefinitionsGroup = _XyzTrapDefinitionsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43993, 3, 1, 2)
)

# Managed Objects groups


# Notification objects

sfcEventDefine = NotificationType(
    (1, 3, 6, 1, 4, 1, 43993, 3, 1, 2, 1)
)
sfcEventDefine.setObjects(
      *(("SFCTRAP-MIB", "sfcEventEntryId"),
        ("SFCTRAP-MIB", "sfcEventEntrySev"),
        ("SFCTRAP-MIB", "sfcEventEntryMsg"),
        ("SFCTRAP-MIB", "sfcEventEntryType"))
)
if mibBuilder.loadTexts:
    sfcEventDefine.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFCTRAP-MIB",
    **{"xyzCorpMib": xyzCorpMib,
       "sfcEventNotify": sfcEventNotify,
       "xyzTrapsGroup": xyzTrapsGroup,
       "xyzTrapObjectsGroup": xyzTrapObjectsGroup,
       "sfcEventEntryId": sfcEventEntryId,
       "sfcEventEntrySev": sfcEventEntrySev,
       "sfcEventEntryMsg": sfcEventEntryMsg,
       "sfcEventEntryType": sfcEventEntryType,
       "xyzTrapDefinitionsGroup": xyzTrapDefinitionsGroup,
       "sfcEventDefine": sfcEventDefine}
)
