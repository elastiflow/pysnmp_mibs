# SNMP MIB module (ManageX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_2427/ManageX-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:30:34 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ManageX_ObjectIdentity = ObjectIdentity
manageX = _ManageX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2427)
)
_MxEvent_ObjectIdentity = ObjectIdentity
mxEvent = _MxEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2427, 1)
)
_MxEventCategory_Type = DisplayString
_MxEventCategory_Object = MibScalar
mxEventCategory = _MxEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 1),
    _MxEventCategory_Type()
)
mxEventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventCategory.setStatus("mandatory")
_MxEventCoMputer_Type = DisplayString
_MxEventCoMputer_Object = MibScalar
mxEventCoMputer = _MxEventCoMputer_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 2),
    _MxEventCoMputer_Type()
)
mxEventCoMputer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventCoMputer.setStatus("mandatory")
_MxEventDescription_Type = DisplayString
_MxEventDescription_Object = MibScalar
mxEventDescription = _MxEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 3),
    _MxEventDescription_Type()
)
mxEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventDescription.setStatus("mandatory")
_MxEventEventId_Type = DisplayString
_MxEventEventId_Object = MibScalar
mxEventEventId = _MxEventEventId_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 4),
    _MxEventEventId_Type()
)
mxEventEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventEventId.setStatus("mandatory")
_MxEventIdentifier_Type = DisplayString
_MxEventIdentifier_Object = MibScalar
mxEventIdentifier = _MxEventIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 5),
    _MxEventIdentifier_Type()
)
mxEventIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventIdentifier.setStatus("mandatory")
_MxEventOriginalTiMe_Type = DisplayString
_MxEventOriginalTiMe_Object = MibScalar
mxEventOriginalTiMe = _MxEventOriginalTiMe_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 6),
    _MxEventOriginalTiMe_Type()
)
mxEventOriginalTiMe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventOriginalTiMe.setStatus("mandatory")
_MxEventRawDescription_Type = DisplayString
_MxEventRawDescription_Object = MibScalar
mxEventRawDescription = _MxEventRawDescription_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 7),
    _MxEventRawDescription_Type()
)
mxEventRawDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventRawDescription.setStatus("mandatory")
_MxEventReceiveCoMputer_Type = DisplayString
_MxEventReceiveCoMputer_Object = MibScalar
mxEventReceiveCoMputer = _MxEventReceiveCoMputer_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 8),
    _MxEventReceiveCoMputer_Type()
)
mxEventReceiveCoMputer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventReceiveCoMputer.setStatus("mandatory")
_MxEventReceiveSource_Type = DisplayString
_MxEventReceiveSource_Object = MibScalar
mxEventReceiveSource = _MxEventReceiveSource_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 9),
    _MxEventReceiveSource_Type()
)
mxEventReceiveSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventReceiveSource.setStatus("mandatory")
_MxEventReceiveTiMe_Type = DisplayString
_MxEventReceiveTiMe_Object = MibScalar
mxEventReceiveTiMe = _MxEventReceiveTiMe_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 10),
    _MxEventReceiveTiMe_Type()
)
mxEventReceiveTiMe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventReceiveTiMe.setStatus("mandatory")
_MxEventSource_Type = DisplayString
_MxEventSource_Object = MibScalar
mxEventSource = _MxEventSource_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 11),
    _MxEventSource_Type()
)
mxEventSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventSource.setStatus("mandatory")
_MxEventStringCount_Type = DisplayString
_MxEventStringCount_Object = MibScalar
mxEventStringCount = _MxEventStringCount_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 12),
    _MxEventStringCount_Type()
)
mxEventStringCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventStringCount.setStatus("mandatory")
_MxEventType_Type = DisplayString
_MxEventType_Object = MibScalar
mxEventType = _MxEventType_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 13),
    _MxEventType_Type()
)
mxEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventType.setStatus("mandatory")
_MxEventUserNaMe_Type = DisplayString
_MxEventUserNaMe_Object = MibScalar
mxEventUserNaMe = _MxEventUserNaMe_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 14),
    _MxEventUserNaMe_Type()
)
mxEventUserNaMe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventUserNaMe.setStatus("mandatory")
_MxEventUserSupplied_Type = DisplayString
_MxEventUserSupplied_Object = MibScalar
mxEventUserSupplied = _MxEventUserSupplied_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 15),
    _MxEventUserSupplied_Type()
)
mxEventUserSupplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventUserSupplied.setStatus("mandatory")
_MxEventStrings_ObjectIdentity = ObjectIdentity
mxEventStrings = _MxEventStrings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100)
)
_MxEventString1_Type = DisplayString
_MxEventString1_Object = MibScalar
mxEventString1 = _MxEventString1_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100, 1),
    _MxEventString1_Type()
)
mxEventString1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventString1.setStatus("mandatory")
_MxEventString2_Type = DisplayString
_MxEventString2_Object = MibScalar
mxEventString2 = _MxEventString2_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100, 2),
    _MxEventString2_Type()
)
mxEventString2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventString2.setStatus("mandatory")
_MxEventString3_Type = DisplayString
_MxEventString3_Object = MibScalar
mxEventString3 = _MxEventString3_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100, 3),
    _MxEventString3_Type()
)
mxEventString3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventString3.setStatus("mandatory")
_MxEventString4_Type = DisplayString
_MxEventString4_Object = MibScalar
mxEventString4 = _MxEventString4_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100, 4),
    _MxEventString4_Type()
)
mxEventString4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventString4.setStatus("mandatory")
_MxEventString5_Type = DisplayString
_MxEventString5_Object = MibScalar
mxEventString5 = _MxEventString5_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100, 5),
    _MxEventString5_Type()
)
mxEventString5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventString5.setStatus("mandatory")
_MxEventString6_Type = DisplayString
_MxEventString6_Object = MibScalar
mxEventString6 = _MxEventString6_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100, 6),
    _MxEventString6_Type()
)
mxEventString6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventString6.setStatus("mandatory")
_MxEventString7_Type = DisplayString
_MxEventString7_Object = MibScalar
mxEventString7 = _MxEventString7_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100, 7),
    _MxEventString7_Type()
)
mxEventString7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventString7.setStatus("mandatory")
_MxEventString8_Type = DisplayString
_MxEventString8_Object = MibScalar
mxEventString8 = _MxEventString8_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100, 8),
    _MxEventString8_Type()
)
mxEventString8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventString8.setStatus("mandatory")
_MxEventString9_Type = DisplayString
_MxEventString9_Object = MibScalar
mxEventString9 = _MxEventString9_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100, 9),
    _MxEventString9_Type()
)
mxEventString9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventString9.setStatus("mandatory")
_MxEventString10_Type = DisplayString
_MxEventString10_Object = MibScalar
mxEventString10 = _MxEventString10_Object(
    (1, 3, 6, 1, 4, 1, 2427, 1, 100, 10),
    _MxEventString10_Type()
)
mxEventString10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mxEventString10.setStatus("mandatory")

# Managed Objects groups


# Notification objects

eventForwarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 0, 1)
)
if mibBuilder.loadTexts:
    eventForwarded.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ManageX-MIB",
    **{"manageX": manageX,
       "eventForwarded": eventForwarded,
       "mxEvent": mxEvent,
       "mxEventCategory": mxEventCategory,
       "mxEventCoMputer": mxEventCoMputer,
       "mxEventDescription": mxEventDescription,
       "mxEventEventId": mxEventEventId,
       "mxEventIdentifier": mxEventIdentifier,
       "mxEventOriginalTiMe": mxEventOriginalTiMe,
       "mxEventRawDescription": mxEventRawDescription,
       "mxEventReceiveCoMputer": mxEventReceiveCoMputer,
       "mxEventReceiveSource": mxEventReceiveSource,
       "mxEventReceiveTiMe": mxEventReceiveTiMe,
       "mxEventSource": mxEventSource,
       "mxEventStringCount": mxEventStringCount,
       "mxEventType": mxEventType,
       "mxEventUserNaMe": mxEventUserNaMe,
       "mxEventUserSupplied": mxEventUserSupplied,
       "mxEventStrings": mxEventStrings,
       "mxEventString1": mxEventString1,
       "mxEventString2": mxEventString2,
       "mxEventString3": mxEventString3,
       "mxEventString4": mxEventString4,
       "mxEventString5": mxEventString5,
       "mxEventString6": mxEventString6,
       "mxEventString7": mxEventString7,
       "mxEventString8": mxEventString8,
       "mxEventString9": mxEventString9,
       "mxEventString10": mxEventString10}
)
