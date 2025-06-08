# SNMP MIB module (WWP-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wwp_6141/WWP-PING-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:32:44 2025
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

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21)
)
if mibBuilder.loadTexts:
    wwpPingMIB.setRevisions(
        ("2001-07-03 12:57",)
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

_WwpPingMIBObjects_ObjectIdentity = ObjectIdentity
wwpPingMIBObjects = _WwpPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1)
)


class _WwpPingDelay_Type(Integer32):
    """Custom type wwpPingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_WwpPingDelay_Type.__name__ = "Integer32"
_WwpPingDelay_Object = MibScalar
wwpPingDelay = _WwpPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 1),
    _WwpPingDelay_Type()
)
wwpPingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPingDelay.setStatus("current")


class _WwpPingPacketSize_Type(Integer32):
    """Custom type wwpPingPacketSize based on Integer32"""
    defaultValue = 56

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1464),
    )


_WwpPingPacketSize_Type.__name__ = "Integer32"
_WwpPingPacketSize_Object = MibScalar
wwpPingPacketSize = _WwpPingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 2),
    _WwpPingPacketSize_Type()
)
wwpPingPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPingPacketSize.setStatus("current")
_WwpPingActivate_Type = TruthValue
_WwpPingActivate_Object = MibScalar
wwpPingActivate = _WwpPingActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 3),
    _WwpPingActivate_Type()
)
wwpPingActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPingActivate.setStatus("current")
_WwpPingAddress_Type = IpAddress
_WwpPingAddress_Object = MibScalar
wwpPingAddress = _WwpPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 4),
    _WwpPingAddress_Type()
)
wwpPingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPingAddress.setStatus("current")


class _WwpPingPacketCount_Type(Integer32):
    """Custom type wwpPingPacketCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_WwpPingPacketCount_Type.__name__ = "Integer32"
_WwpPingPacketCount_Object = MibScalar
wwpPingPacketCount = _WwpPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 5),
    _WwpPingPacketCount_Type()
)
wwpPingPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPingPacketCount.setStatus("current")


class _WwpPingPacketTimeout_Type(Integer32):
    """Custom type wwpPingPacketTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_WwpPingPacketTimeout_Type.__name__ = "Integer32"
_WwpPingPacketTimeout_Object = MibScalar
wwpPingPacketTimeout = _WwpPingPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 6),
    _WwpPingPacketTimeout_Type()
)
wwpPingPacketTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPingPacketTimeout.setStatus("current")
_WwpPingSentPackets_Type = Counter32
_WwpPingSentPackets_Object = MibScalar
wwpPingSentPackets = _WwpPingSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 8),
    _WwpPingSentPackets_Type()
)
wwpPingSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPingSentPackets.setStatus("current")
_WwpPingReceivedPackets_Type = Counter32
_WwpPingReceivedPackets_Object = MibScalar
wwpPingReceivedPackets = _WwpPingReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 9),
    _WwpPingReceivedPackets_Type()
)
wwpPingReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPingReceivedPackets.setStatus("current")
_WwpPingFailCause_Type = PingFailCause
_WwpPingFailCause_Object = MibScalar
wwpPingFailCause = _WwpPingFailCause_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 13),
    _WwpPingFailCause_Type()
)
wwpPingFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPingFailCause.setStatus("current")


class _WwpPingState_Type(PingState):
    """Custom type wwpPingState based on PingState"""
    defaultValue = 1


_WwpPingState_Type.__name__ = "PingState"
_WwpPingState_Object = MibScalar
wwpPingState = _WwpPingState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 15),
    _WwpPingState_Type()
)
wwpPingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPingState.setStatus("current")


class _WwpPingUntilStopped_Type(TruthValue):
    """Custom type wwpPingUntilStopped based on TruthValue"""
    defaultValue = 2


_WwpPingUntilStopped_Type.__name__ = "TruthValue"
_WwpPingUntilStopped_Object = MibScalar
wwpPingUntilStopped = _WwpPingUntilStopped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 16),
    _WwpPingUntilStopped_Type()
)
wwpPingUntilStopped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpPingUntilStopped.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-PING-MIB",
    **{"PingFailCause": PingFailCause,
       "PingState": PingState,
       "wwpPingMIB": wwpPingMIB,
       "wwpPingMIBObjects": wwpPingMIBObjects,
       "wwpPingDelay": wwpPingDelay,
       "wwpPingPacketSize": wwpPingPacketSize,
       "wwpPingActivate": wwpPingActivate,
       "wwpPingAddress": wwpPingAddress,
       "wwpPingPacketCount": wwpPingPacketCount,
       "wwpPingPacketTimeout": wwpPingPacketTimeout,
       "wwpPingSentPackets": wwpPingSentPackets,
       "wwpPingReceivedPackets": wwpPingReceivedPackets,
       "wwpPingFailCause": wwpPingFailCause,
       "wwpPingState": wwpPingState,
       "wwpPingUntilStopped": wwpPingUntilStopped}
)
