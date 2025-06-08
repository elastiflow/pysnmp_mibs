# SNMP MIB module (MIOX25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/MIOX25-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:42:48 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InstancePointer,) = mibBuilder.importSymbols(
    "RFC1316-MIB",
    "InstancePointer")

(PositiveInteger,) = mibBuilder.importSymbols(
    "RFC1381-MIB",
    "PositiveInteger")

(X121Address,) = mibBuilder.importSymbols(
    "RFC1382-MIB",
    "X121Address")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

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

_Miox_ObjectIdentity = ObjectIdentity
miox = _Miox_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 38)
)
_MioxPle_ObjectIdentity = ObjectIdentity
mioxPle = _MioxPle_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 38, 1)
)
_MioxPleTable_Object = MibTable
mioxPleTable = _MioxPleTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1)
)
if mibBuilder.loadTexts:
    mioxPleTable.setStatus("mandatory")
_MioxPleEntry_Object = MibTableRow
mioxPleEntry = _MioxPleEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1)
)
mioxPleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mioxPleEntry.setStatus("mandatory")


class _MioxPleMaxCircuits_Type(Integer32):
    """Custom type mioxPleMaxCircuits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MioxPleMaxCircuits_Type.__name__ = "Integer32"
_MioxPleMaxCircuits_Object = MibTableColumn
mioxPleMaxCircuits = _MioxPleMaxCircuits_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 1),
    _MioxPleMaxCircuits_Type()
)
mioxPleMaxCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPleMaxCircuits.setStatus("mandatory")
_MioxPleRefusedConnections_Type = Counter32
_MioxPleRefusedConnections_Object = MibTableColumn
mioxPleRefusedConnections = _MioxPleRefusedConnections_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 2),
    _MioxPleRefusedConnections_Type()
)
mioxPleRefusedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPleRefusedConnections.setStatus("mandatory")
_MioxPleEnAddrToX121LkupFlrs_Type = Counter32
_MioxPleEnAddrToX121LkupFlrs_Object = MibTableColumn
mioxPleEnAddrToX121LkupFlrs = _MioxPleEnAddrToX121LkupFlrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 3),
    _MioxPleEnAddrToX121LkupFlrs_Type()
)
mioxPleEnAddrToX121LkupFlrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPleEnAddrToX121LkupFlrs.setStatus("mandatory")


class _MioxPleLastFailedEnAddr_Type(OctetString):
    """Custom type mioxPleLastFailedEnAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_MioxPleLastFailedEnAddr_Type.__name__ = "OctetString"
_MioxPleLastFailedEnAddr_Object = MibTableColumn
mioxPleLastFailedEnAddr = _MioxPleLastFailedEnAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 4),
    _MioxPleLastFailedEnAddr_Type()
)
mioxPleLastFailedEnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPleLastFailedEnAddr.setStatus("mandatory")
_MioxPleEnAddrToX121LkupFlrTime_Type = TimeTicks
_MioxPleEnAddrToX121LkupFlrTime_Object = MibTableColumn
mioxPleEnAddrToX121LkupFlrTime = _MioxPleEnAddrToX121LkupFlrTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 5),
    _MioxPleEnAddrToX121LkupFlrTime_Type()
)
mioxPleEnAddrToX121LkupFlrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPleEnAddrToX121LkupFlrTime.setStatus("mandatory")
_MioxPleX121ToEnAddrLkupFlrs_Type = Counter32
_MioxPleX121ToEnAddrLkupFlrs_Object = MibTableColumn
mioxPleX121ToEnAddrLkupFlrs = _MioxPleX121ToEnAddrLkupFlrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 6),
    _MioxPleX121ToEnAddrLkupFlrs_Type()
)
mioxPleX121ToEnAddrLkupFlrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPleX121ToEnAddrLkupFlrs.setStatus("mandatory")
_MioxPleLastFailedX121Address_Type = X121Address
_MioxPleLastFailedX121Address_Object = MibTableColumn
mioxPleLastFailedX121Address = _MioxPleLastFailedX121Address_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 7),
    _MioxPleLastFailedX121Address_Type()
)
mioxPleLastFailedX121Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPleLastFailedX121Address.setStatus("mandatory")
_MioxPleX121ToEnAddrLkupFlrTime_Type = TimeTicks
_MioxPleX121ToEnAddrLkupFlrTime_Object = MibTableColumn
mioxPleX121ToEnAddrLkupFlrTime = _MioxPleX121ToEnAddrLkupFlrTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 8),
    _MioxPleX121ToEnAddrLkupFlrTime_Type()
)
mioxPleX121ToEnAddrLkupFlrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPleX121ToEnAddrLkupFlrTime.setStatus("mandatory")
_MioxPleQbitFailures_Type = Counter32
_MioxPleQbitFailures_Object = MibTableColumn
mioxPleQbitFailures = _MioxPleQbitFailures_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 9),
    _MioxPleQbitFailures_Type()
)
mioxPleQbitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPleQbitFailures.setStatus("mandatory")
_MioxPleQbitFailureRemoteAddress_Type = X121Address
_MioxPleQbitFailureRemoteAddress_Object = MibTableColumn
mioxPleQbitFailureRemoteAddress = _MioxPleQbitFailureRemoteAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 10),
    _MioxPleQbitFailureRemoteAddress_Type()
)
mioxPleQbitFailureRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPleQbitFailureRemoteAddress.setStatus("mandatory")
_MioxPleQbitFailureTime_Type = TimeTicks
_MioxPleQbitFailureTime_Object = MibTableColumn
mioxPleQbitFailureTime = _MioxPleQbitFailureTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 11),
    _MioxPleQbitFailureTime_Type()
)
mioxPleQbitFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPleQbitFailureTime.setStatus("mandatory")


class _MioxPleMinimumOpenTimer_Type(PositiveInteger):
    """Custom type mioxPleMinimumOpenTimer based on PositiveInteger"""
    defaultValue = 0


_MioxPleMinimumOpenTimer_Type.__name__ = "PositiveInteger"
_MioxPleMinimumOpenTimer_Object = MibTableColumn
mioxPleMinimumOpenTimer = _MioxPleMinimumOpenTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 12),
    _MioxPleMinimumOpenTimer_Type()
)
mioxPleMinimumOpenTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPleMinimumOpenTimer.setStatus("mandatory")


class _MioxPleInactivityTimer_Type(PositiveInteger):
    """Custom type mioxPleInactivityTimer based on PositiveInteger"""
    defaultValue = 10000


_MioxPleInactivityTimer_Type.__name__ = "PositiveInteger"
_MioxPleInactivityTimer_Object = MibTableColumn
mioxPleInactivityTimer = _MioxPleInactivityTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 13),
    _MioxPleInactivityTimer_Type()
)
mioxPleInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPleInactivityTimer.setStatus("mandatory")


class _MioxPleHoldDownTimer_Type(PositiveInteger):
    """Custom type mioxPleHoldDownTimer based on PositiveInteger"""
    defaultValue = 0


_MioxPleHoldDownTimer_Type.__name__ = "PositiveInteger"
_MioxPleHoldDownTimer_Object = MibTableColumn
mioxPleHoldDownTimer = _MioxPleHoldDownTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 14),
    _MioxPleHoldDownTimer_Type()
)
mioxPleHoldDownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPleHoldDownTimer.setStatus("mandatory")


class _MioxPleCollisionRetryTimer_Type(PositiveInteger):
    """Custom type mioxPleCollisionRetryTimer based on PositiveInteger"""
    defaultValue = 0


_MioxPleCollisionRetryTimer_Type.__name__ = "PositiveInteger"
_MioxPleCollisionRetryTimer_Object = MibTableColumn
mioxPleCollisionRetryTimer = _MioxPleCollisionRetryTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 15),
    _MioxPleCollisionRetryTimer_Type()
)
mioxPleCollisionRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPleCollisionRetryTimer.setStatus("mandatory")
_MioxPleDefaultPeerId_Type = InstancePointer
_MioxPleDefaultPeerId_Object = MibTableColumn
mioxPleDefaultPeerId = _MioxPleDefaultPeerId_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 1, 1, 1, 16),
    _MioxPleDefaultPeerId_Type()
)
mioxPleDefaultPeerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPleDefaultPeerId.setStatus("mandatory")
_MioxPeer_ObjectIdentity = ObjectIdentity
mioxPeer = _MioxPeer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 38, 2)
)
_MioxPeerTable_Object = MibTable
mioxPeerTable = _MioxPeerTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1)
)
if mibBuilder.loadTexts:
    mioxPeerTable.setStatus("mandatory")
_MioxPeerEntry_Object = MibTableRow
mioxPeerEntry = _MioxPeerEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1)
)
mioxPeerEntry.setIndexNames(
    (0, "MIOX25-MIB", "mioxPeerIndex"),
)
if mibBuilder.loadTexts:
    mioxPeerEntry.setStatus("mandatory")
_MioxPeerIndex_Type = PositiveInteger
_MioxPeerIndex_Object = MibTableColumn
mioxPeerIndex = _MioxPeerIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 1),
    _MioxPeerIndex_Type()
)
mioxPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPeerIndex.setStatus("mandatory")


class _MioxPeerStatus_Type(Integer32):
    """Custom type mioxPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4),
          ("clearCall", 5),
          ("makeCall", 6))
    )


_MioxPeerStatus_Type.__name__ = "Integer32"
_MioxPeerStatus_Object = MibTableColumn
mioxPeerStatus = _MioxPeerStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 2),
    _MioxPeerStatus_Type()
)
mioxPeerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPeerStatus.setStatus("mandatory")


class _MioxPeerMaxCircuits_Type(PositiveInteger):
    """Custom type mioxPeerMaxCircuits based on PositiveInteger"""
    defaultValue = 1


_MioxPeerMaxCircuits_Type.__name__ = "PositiveInteger"
_MioxPeerMaxCircuits_Object = MibTableColumn
mioxPeerMaxCircuits = _MioxPeerMaxCircuits_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 3),
    _MioxPeerMaxCircuits_Type()
)
mioxPeerMaxCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPeerMaxCircuits.setStatus("mandatory")


class _MioxPeerIfIndex_Type(PositiveInteger):
    """Custom type mioxPeerIfIndex based on PositiveInteger"""
    defaultValue = 1


_MioxPeerIfIndex_Type.__name__ = "PositiveInteger"
_MioxPeerIfIndex_Object = MibTableColumn
mioxPeerIfIndex = _MioxPeerIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 4),
    _MioxPeerIfIndex_Type()
)
mioxPeerIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPeerIfIndex.setStatus("mandatory")
_MioxPeerConnectSeconds_Type = Counter32
_MioxPeerConnectSeconds_Object = MibTableColumn
mioxPeerConnectSeconds = _MioxPeerConnectSeconds_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 5),
    _MioxPeerConnectSeconds_Type()
)
mioxPeerConnectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPeerConnectSeconds.setStatus("mandatory")
_MioxPeerX25CallParamId_Type = InstancePointer
_MioxPeerX25CallParamId_Object = MibTableColumn
mioxPeerX25CallParamId = _MioxPeerX25CallParamId_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 6),
    _MioxPeerX25CallParamId_Type()
)
mioxPeerX25CallParamId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPeerX25CallParamId.setStatus("mandatory")


class _MioxPeerEnAddr_Type(OctetString):
    """Custom type mioxPeerEnAddr based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MioxPeerEnAddr_Type.__name__ = "OctetString"
_MioxPeerEnAddr_Object = MibTableColumn
mioxPeerEnAddr = _MioxPeerEnAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 7),
    _MioxPeerEnAddr_Type()
)
mioxPeerEnAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPeerEnAddr.setStatus("mandatory")


class _MioxPeerX121Address_Type(X121Address):
    """Custom type mioxPeerX121Address based on X121Address"""
    defaultHexValue = ""


_MioxPeerX121Address_Type.__name__ = "X121Address"
_MioxPeerX121Address_Object = MibTableColumn
mioxPeerX121Address = _MioxPeerX121Address_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 8),
    _MioxPeerX121Address_Type()
)
mioxPeerX121Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPeerX121Address.setStatus("mandatory")
_MioxPeerX25CircuitId_Type = InstancePointer
_MioxPeerX25CircuitId_Object = MibTableColumn
mioxPeerX25CircuitId = _MioxPeerX25CircuitId_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 9),
    _MioxPeerX25CircuitId_Type()
)
mioxPeerX25CircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPeerX25CircuitId.setStatus("mandatory")


class _MioxPeerDescr_Type(DisplayString):
    """Custom type mioxPeerDescr based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MioxPeerDescr_Type.__name__ = "DisplayString"
_MioxPeerDescr_Object = MibTableColumn
mioxPeerDescr = _MioxPeerDescr_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 1, 1, 10),
    _MioxPeerDescr_Type()
)
mioxPeerDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPeerDescr.setStatus("mandatory")
_MioxPeerEncTable_Object = MibTable
mioxPeerEncTable = _MioxPeerEncTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 2)
)
if mibBuilder.loadTexts:
    mioxPeerEncTable.setStatus("mandatory")
_MioxPeerEncEntry_Object = MibTableRow
mioxPeerEncEntry = _MioxPeerEncEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1)
)
mioxPeerEncEntry.setIndexNames(
    (0, "MIOX25-MIB", "mioxPeerIndex"),
    (0, "MIOX25-MIB", "mioxPeerEncIndex"),
)
if mibBuilder.loadTexts:
    mioxPeerEncEntry.setStatus("mandatory")
_MioxPeerEncIndex_Type = PositiveInteger
_MioxPeerEncIndex_Object = MibTableColumn
mioxPeerEncIndex = _MioxPeerEncIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1, 1),
    _MioxPeerEncIndex_Type()
)
mioxPeerEncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mioxPeerEncIndex.setStatus("mandatory")


class _MioxPeerEncType_Type(Integer32):
    """Custom type mioxPeerEncType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MioxPeerEncType_Type.__name__ = "Integer32"
_MioxPeerEncType_Object = MibTableColumn
mioxPeerEncType = _MioxPeerEncType_Object(
    (1, 3, 6, 1, 2, 1, 10, 38, 2, 2, 1, 2),
    _MioxPeerEncType_Type()
)
mioxPeerEncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mioxPeerEncType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIOX25-MIB",
    **{"miox": miox,
       "mioxPle": mioxPle,
       "mioxPleTable": mioxPleTable,
       "mioxPleEntry": mioxPleEntry,
       "mioxPleMaxCircuits": mioxPleMaxCircuits,
       "mioxPleRefusedConnections": mioxPleRefusedConnections,
       "mioxPleEnAddrToX121LkupFlrs": mioxPleEnAddrToX121LkupFlrs,
       "mioxPleLastFailedEnAddr": mioxPleLastFailedEnAddr,
       "mioxPleEnAddrToX121LkupFlrTime": mioxPleEnAddrToX121LkupFlrTime,
       "mioxPleX121ToEnAddrLkupFlrs": mioxPleX121ToEnAddrLkupFlrs,
       "mioxPleLastFailedX121Address": mioxPleLastFailedX121Address,
       "mioxPleX121ToEnAddrLkupFlrTime": mioxPleX121ToEnAddrLkupFlrTime,
       "mioxPleQbitFailures": mioxPleQbitFailures,
       "mioxPleQbitFailureRemoteAddress": mioxPleQbitFailureRemoteAddress,
       "mioxPleQbitFailureTime": mioxPleQbitFailureTime,
       "mioxPleMinimumOpenTimer": mioxPleMinimumOpenTimer,
       "mioxPleInactivityTimer": mioxPleInactivityTimer,
       "mioxPleHoldDownTimer": mioxPleHoldDownTimer,
       "mioxPleCollisionRetryTimer": mioxPleCollisionRetryTimer,
       "mioxPleDefaultPeerId": mioxPleDefaultPeerId,
       "mioxPeer": mioxPeer,
       "mioxPeerTable": mioxPeerTable,
       "mioxPeerEntry": mioxPeerEntry,
       "mioxPeerIndex": mioxPeerIndex,
       "mioxPeerStatus": mioxPeerStatus,
       "mioxPeerMaxCircuits": mioxPeerMaxCircuits,
       "mioxPeerIfIndex": mioxPeerIfIndex,
       "mioxPeerConnectSeconds": mioxPeerConnectSeconds,
       "mioxPeerX25CallParamId": mioxPeerX25CallParamId,
       "mioxPeerEnAddr": mioxPeerEnAddr,
       "mioxPeerX121Address": mioxPeerX121Address,
       "mioxPeerX25CircuitId": mioxPeerX25CircuitId,
       "mioxPeerDescr": mioxPeerDescr,
       "mioxPeerEncTable": mioxPeerEncTable,
       "mioxPeerEncEntry": mioxPeerEncEntry,
       "mioxPeerEncIndex": mioxPeerEncIndex,
       "mioxPeerEncType": mioxPeerEncType}
)
