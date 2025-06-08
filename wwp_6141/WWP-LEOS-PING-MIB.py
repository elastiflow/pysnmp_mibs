# SNMP MIB module (WWP-LEOS-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wwp_6141/WWP-LEOS-PING-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:32:54 2025
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19)
)
if mibBuilder.loadTexts:
    wwpLeosPingMIB.setRevisions(
        ("2013-04-26 00:00",
         "2012-04-02 00:00",
         "2001-07-03 12:57")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PingFailCause(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("unknownHost", 1),
          ("socketError", 2),
          ("bindError", 3),
          ("connectError", 4),
          ("missingHost", 5),
          ("asyncError", 6),
          ("nonBlockError", 7),
          ("mcastError", 8),
          ("ttlError", 9),
          ("mcastTtlError", 10),
          ("outputError", 11),
          ("unreachableError", 12),
          ("isAlive", 13),
          ("txRx", 14),
          ("commandCompleted", 15),
          ("noStatus", 16),
          ("sendRecvMismatch", 17))
    )



class PingState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("pinging", 2),
          ("pingComplete", 3),
          ("failed", 4))
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosPingMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosPingMIBObjects = _WwpLeosPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1)
)


class _WwpLeosPingDelay_Type(Integer32):
    """Custom type wwpLeosPingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_WwpLeosPingDelay_Type.__name__ = "Integer32"
_WwpLeosPingDelay_Object = MibScalar
wwpLeosPingDelay = _WwpLeosPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 1),
    _WwpLeosPingDelay_Type()
)
wwpLeosPingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingDelay.setStatus("current")


class _WwpLeosPingPacketSize_Type(Integer32):
    """Custom type wwpLeosPingPacketSize based on Integer32"""
    defaultValue = 56

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1464),
    )


_WwpLeosPingPacketSize_Type.__name__ = "Integer32"
_WwpLeosPingPacketSize_Object = MibScalar
wwpLeosPingPacketSize = _WwpLeosPingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 2),
    _WwpLeosPingPacketSize_Type()
)
wwpLeosPingPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingPacketSize.setStatus("current")
_WwpLeosPingActivate_Type = TruthValue
_WwpLeosPingActivate_Object = MibScalar
wwpLeosPingActivate = _WwpLeosPingActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 3),
    _WwpLeosPingActivate_Type()
)
wwpLeosPingActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingActivate.setStatus("current")
_WwpLeosPingAddrType_Type = AddressFamilyNumbers
_WwpLeosPingAddrType_Object = MibScalar
wwpLeosPingAddrType = _WwpLeosPingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 4),
    _WwpLeosPingAddrType_Type()
)
wwpLeosPingAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingAddrType.setStatus("current")
_WwpLeosPingAddr_Type = DisplayString
_WwpLeosPingAddr_Object = MibScalar
wwpLeosPingAddr = _WwpLeosPingAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 5),
    _WwpLeosPingAddr_Type()
)
wwpLeosPingAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingAddr.setStatus("current")


class _WwpLeosPingPacketCount_Type(Integer32):
    """Custom type wwpLeosPingPacketCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_WwpLeosPingPacketCount_Type.__name__ = "Integer32"
_WwpLeosPingPacketCount_Object = MibScalar
wwpLeosPingPacketCount = _WwpLeosPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 6),
    _WwpLeosPingPacketCount_Type()
)
wwpLeosPingPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingPacketCount.setStatus("current")


class _WwpLeosPingPacketTimeout_Type(Integer32):
    """Custom type wwpLeosPingPacketTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_WwpLeosPingPacketTimeout_Type.__name__ = "Integer32"
_WwpLeosPingPacketTimeout_Object = MibScalar
wwpLeosPingPacketTimeout = _WwpLeosPingPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 7),
    _WwpLeosPingPacketTimeout_Type()
)
wwpLeosPingPacketTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingPacketTimeout.setStatus("current")
_WwpLeosPingSentPackets_Type = Counter32
_WwpLeosPingSentPackets_Object = MibScalar
wwpLeosPingSentPackets = _WwpLeosPingSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 8),
    _WwpLeosPingSentPackets_Type()
)
wwpLeosPingSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingSentPackets.setStatus("current")
_WwpLeosPingReceivedPackets_Type = Counter32
_WwpLeosPingReceivedPackets_Object = MibScalar
wwpLeosPingReceivedPackets = _WwpLeosPingReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 9),
    _WwpLeosPingReceivedPackets_Type()
)
wwpLeosPingReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingReceivedPackets.setStatus("current")
_WwpLeosPingFailCause_Type = PingFailCause
_WwpLeosPingFailCause_Object = MibScalar
wwpLeosPingFailCause = _WwpLeosPingFailCause_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 10),
    _WwpLeosPingFailCause_Type()
)
wwpLeosPingFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingFailCause.setStatus("current")


class _WwpLeosPingState_Type(PingState):
    """Custom type wwpLeosPingState based on PingState"""
    defaultValue = 1


_WwpLeosPingState_Type.__name__ = "PingState"
_WwpLeosPingState_Object = MibScalar
wwpLeosPingState = _WwpLeosPingState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 11),
    _WwpLeosPingState_Type()
)
wwpLeosPingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingState.setStatus("current")


class _WwpLeosPingUntilStopped_Type(TruthValue):
    """Custom type wwpLeosPingUntilStopped based on TruthValue"""
    defaultValue = 2


_WwpLeosPingUntilStopped_Type.__name__ = "TruthValue"
_WwpLeosPingUntilStopped_Object = MibScalar
wwpLeosPingUntilStopped = _WwpLeosPingUntilStopped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 12),
    _WwpLeosPingUntilStopped_Type()
)
wwpLeosPingUntilStopped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPingUntilStopped.setStatus("current")
_WwpLeosPingInetAddrType_Type = InetAddressType
_WwpLeosPingInetAddrType_Object = MibScalar
wwpLeosPingInetAddrType = _WwpLeosPingInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 13),
    _WwpLeosPingInetAddrType_Type()
)
wwpLeosPingInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPingInetAddrType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-PING-MIB",
    **{"PingFailCause": PingFailCause,
       "PingState": PingState,
       "wwpLeosPingMIB": wwpLeosPingMIB,
       "wwpLeosPingMIBObjects": wwpLeosPingMIBObjects,
       "wwpLeosPingDelay": wwpLeosPingDelay,
       "wwpLeosPingPacketSize": wwpLeosPingPacketSize,
       "wwpLeosPingActivate": wwpLeosPingActivate,
       "wwpLeosPingAddrType": wwpLeosPingAddrType,
       "wwpLeosPingAddr": wwpLeosPingAddr,
       "wwpLeosPingPacketCount": wwpLeosPingPacketCount,
       "wwpLeosPingPacketTimeout": wwpLeosPingPacketTimeout,
       "wwpLeosPingSentPackets": wwpLeosPingSentPackets,
       "wwpLeosPingReceivedPackets": wwpLeosPingReceivedPackets,
       "wwpLeosPingFailCause": wwpLeosPingFailCause,
       "wwpLeosPingState": wwpLeosPingState,
       "wwpLeosPingUntilStopped": wwpLeosPingUntilStopped,
       "wwpLeosPingInetAddrType": wwpLeosPingInetAddrType}
)
