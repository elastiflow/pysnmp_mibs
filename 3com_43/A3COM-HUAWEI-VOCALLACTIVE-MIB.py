# SNMP MIB module (A3COM-HUAWEI-VOCALLACTIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-VOCALLACTIVE-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:00:40 2025
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

(h3cVoice,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cVoice")

(CodecType,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-VO-TYPE-MIB",
    "CodecType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

h3cVoiceCallActive = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6)
)
if mibBuilder.loadTexts:
    h3cVoiceCallActive.setRevisions(
        ("2005-03-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoCallActiveObjects_ObjectIdentity = ObjectIdentity
h3cVoCallActiveObjects = _H3cVoCallActiveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1)
)
_H3cVoCallActiveTable_Object = MibTable
h3cVoCallActiveTable = _H3cVoCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVoCallActiveTable.setStatus("current")
_H3cVoCallActiveEntry_Object = MibTableRow
h3cVoCallActiveEntry = _H3cVoCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1)
)
h3cVoCallActiveEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOCALLACTIVE-MIB", "h3cVoCallActiveChannel"),
)
if mibBuilder.loadTexts:
    h3cVoCallActiveEntry.setStatus("current")
_H3cVoCallActiveChannel_Type = Integer32
_H3cVoCallActiveChannel_Object = MibTableColumn
h3cVoCallActiveChannel = _H3cVoCallActiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 1),
    _H3cVoCallActiveChannel_Type()
)
h3cVoCallActiveChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoCallActiveChannel.setStatus("current")
_H3cVoCallActiveCallerNumber_Type = OctetString
_H3cVoCallActiveCallerNumber_Object = MibTableColumn
h3cVoCallActiveCallerNumber = _H3cVoCallActiveCallerNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 2),
    _H3cVoCallActiveCallerNumber_Type()
)
h3cVoCallActiveCallerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveCallerNumber.setStatus("current")
_H3cVoCallActiveCalledNumber_Type = OctetString
_H3cVoCallActiveCalledNumber_Object = MibTableColumn
h3cVoCallActiveCalledNumber = _H3cVoCallActiveCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 3),
    _H3cVoCallActiveCalledNumber_Type()
)
h3cVoCallActiveCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveCalledNumber.setStatus("current")
_H3cVoCallActiveEncodeType_Type = CodecType
_H3cVoCallActiveEncodeType_Object = MibTableColumn
h3cVoCallActiveEncodeType = _H3cVoCallActiveEncodeType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 4),
    _H3cVoCallActiveEncodeType_Type()
)
h3cVoCallActiveEncodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveEncodeType.setStatus("current")
_H3cVoCallActiveLocalAddressType_Type = InetAddressType
_H3cVoCallActiveLocalAddressType_Object = MibTableColumn
h3cVoCallActiveLocalAddressType = _H3cVoCallActiveLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 5),
    _H3cVoCallActiveLocalAddressType_Type()
)
h3cVoCallActiveLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveLocalAddressType.setStatus("current")
_H3cVoCallActiveLocalAddress_Type = InetAddress
_H3cVoCallActiveLocalAddress_Object = MibTableColumn
h3cVoCallActiveLocalAddress = _H3cVoCallActiveLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 6),
    _H3cVoCallActiveLocalAddress_Type()
)
h3cVoCallActiveLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveLocalAddress.setStatus("current")
_H3cVoCallActivePeerAddressType_Type = InetAddressType
_H3cVoCallActivePeerAddressType_Object = MibTableColumn
h3cVoCallActivePeerAddressType = _H3cVoCallActivePeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 7),
    _H3cVoCallActivePeerAddressType_Type()
)
h3cVoCallActivePeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActivePeerAddressType.setStatus("current")
_H3cVoCallActivePeerAddress_Type = InetAddress
_H3cVoCallActivePeerAddress_Object = MibTableColumn
h3cVoCallActivePeerAddress = _H3cVoCallActivePeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 8),
    _H3cVoCallActivePeerAddress_Type()
)
h3cVoCallActivePeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActivePeerAddress.setStatus("current")


class _H3cVoCallActiveCallOrigin_Type(Integer32):
    """Custom type h3cVoCallActiveCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("caller", 1),
          ("called", 2))
    )


_H3cVoCallActiveCallOrigin_Type.__name__ = "Integer32"
_H3cVoCallActiveCallOrigin_Object = MibTableColumn
h3cVoCallActiveCallOrigin = _H3cVoCallActiveCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 9),
    _H3cVoCallActiveCallOrigin_Type()
)
h3cVoCallActiveCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveCallOrigin.setStatus("current")


class _H3cVoCallActiveIPSigType_Type(Integer32):
    """Custom type h3cVoCallActiveIPSigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("h323", 2),
          ("sip", 3))
    )


_H3cVoCallActiveIPSigType_Type.__name__ = "Integer32"
_H3cVoCallActiveIPSigType_Object = MibTableColumn
h3cVoCallActiveIPSigType = _H3cVoCallActiveIPSigType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 10),
    _H3cVoCallActiveIPSigType_Type()
)
h3cVoCallActiveIPSigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveIPSigType.setStatus("current")


class _H3cVoCallActivePSTNSigType_Type(Integer32):
    """Custom type h3cVoCallActivePSTNSigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("fxs", 2),
          ("fxo", 3),
          ("em", 4),
          ("r2", 5),
          ("dss1", 6),
          ("dem", 7))
    )


_H3cVoCallActivePSTNSigType_Type.__name__ = "Integer32"
_H3cVoCallActivePSTNSigType_Object = MibTableColumn
h3cVoCallActivePSTNSigType = _H3cVoCallActivePSTNSigType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 11),
    _H3cVoCallActivePSTNSigType_Type()
)
h3cVoCallActivePSTNSigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActivePSTNSigType.setStatus("current")


class _H3cVoCallActiveStatus_Type(Integer32):
    """Custom type h3cVoCallActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("calling", 2),
          ("alerting", 3),
          ("talking", 4),
          ("release", 5))
    )


_H3cVoCallActiveStatus_Type.__name__ = "Integer32"
_H3cVoCallActiveStatus_Object = MibTableColumn
h3cVoCallActiveStatus = _H3cVoCallActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 6, 1, 1, 1, 12),
    _H3cVoCallActiveStatus_Type()
)
h3cVoCallActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoCallActiveStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-VOCALLACTIVE-MIB",
    **{"h3cVoiceCallActive": h3cVoiceCallActive,
       "h3cVoCallActiveObjects": h3cVoCallActiveObjects,
       "h3cVoCallActiveTable": h3cVoCallActiveTable,
       "h3cVoCallActiveEntry": h3cVoCallActiveEntry,
       "h3cVoCallActiveChannel": h3cVoCallActiveChannel,
       "h3cVoCallActiveCallerNumber": h3cVoCallActiveCallerNumber,
       "h3cVoCallActiveCalledNumber": h3cVoCallActiveCalledNumber,
       "h3cVoCallActiveEncodeType": h3cVoCallActiveEncodeType,
       "h3cVoCallActiveLocalAddressType": h3cVoCallActiveLocalAddressType,
       "h3cVoCallActiveLocalAddress": h3cVoCallActiveLocalAddress,
       "h3cVoCallActivePeerAddressType": h3cVoCallActivePeerAddressType,
       "h3cVoCallActivePeerAddress": h3cVoCallActivePeerAddress,
       "h3cVoCallActiveCallOrigin": h3cVoCallActiveCallOrigin,
       "h3cVoCallActiveIPSigType": h3cVoCallActiveIPSigType,
       "h3cVoCallActivePSTNSigType": h3cVoCallActivePSTNSigType,
       "h3cVoCallActiveStatus": h3cVoCallActiveStatus}
)
