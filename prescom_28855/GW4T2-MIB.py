# SNMP MIB module (GW4T2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/prescom_28855/GW4T2-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:58:11 2025
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

gatewaygw4t2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3)
)
if mibBuilder.loadTexts:
    gatewaygw4t2.setRevisions(
        ("2015-12-18 00:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Tgw4t2ChanState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("stateIdle", 0),
          ("stateIn", 1),
          ("stateOut", 2),
          ("stateNotUsed", 9))
    )



class Tgw4t2sipAccountStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("registered", 0),
          ("notregistered", 1),
          ("unused", 2),
          ("noregistration", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Gw4t2_ObjectIdentity = ObjectIdentity
gw4t2 = _Gw4t2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1)
)
_Gw4t2Version_ObjectIdentity = ObjectIdentity
gw4t2Version = _Gw4t2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 1)
)


class _Gw4t2VersionString_Type(DisplayString):
    """Custom type gw4t2VersionString based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gw4t2VersionString_Type.__name__ = "DisplayString"
_Gw4t2VersionString_Object = MibScalar
gw4t2VersionString = _Gw4t2VersionString_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 1, 1),
    _Gw4t2VersionString_Type()
)
gw4t2VersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2VersionString.setStatus("current")
_Gw4t2Status_ObjectIdentity = ObjectIdentity
gw4t2Status = _Gw4t2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 2)
)


class _Gw4t2GlobalStatus_Type(Integer):
    """Custom type gw4t2GlobalStatus based on Integer"""
    defaultValue = 0

    subtypeSpec = Integer.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Starting", 0),
          ("Ready", 1),
          ("OK", 2))
    )


_Gw4t2GlobalStatus_Type.__name__ = "Integer"
_Gw4t2GlobalStatus_Object = MibScalar
gw4t2GlobalStatus = _Gw4t2GlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 2, 1),
    _Gw4t2GlobalStatus_Type()
)
gw4t2GlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2GlobalStatus.setStatus("current")


class _Gw4t2Autotests_Type(DisplayString):
    """Custom type gw4t2Autotests based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gw4t2Autotests_Type.__name__ = "DisplayString"
_Gw4t2Autotests_Object = MibScalar
gw4t2Autotests = _Gw4t2Autotests_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 2, 2),
    _Gw4t2Autotests_Type()
)
gw4t2Autotests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2Autotests.setStatus("current")
_Gw4t2Channels_ObjectIdentity = ObjectIdentity
gw4t2Channels = _Gw4t2Channels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 3)
)
_Gw4t2NumChannels_Type = Integer32
_Gw4t2NumChannels_Object = MibScalar
gw4t2NumChannels = _Gw4t2NumChannels_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 3, 1),
    _Gw4t2NumChannels_Type()
)
gw4t2NumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2NumChannels.setStatus("current")
_Gw4t2ChanTable_Object = MibTable
gw4t2ChanTable = _Gw4t2ChanTable_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gw4t2ChanTable.setStatus("current")
_Gw4t2ChanEntry_Object = MibTableRow
gw4t2ChanEntry = _Gw4t2ChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 3, 2, 1)
)
gw4t2ChanEntry.setIndexNames(
    (0, "GW4T2-MIB", "gw4t2ChanIndex"),
)
if mibBuilder.loadTexts:
    gw4t2ChanEntry.setStatus("current")


class _Gw4t2ChanIndex_Type(Integer32):
    """Custom type gw4t2ChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gw4t2ChanIndex_Type.__name__ = "Integer32"
_Gw4t2ChanIndex_Object = MibTableColumn
gw4t2ChanIndex = _Gw4t2ChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 3, 2, 1, 1),
    _Gw4t2ChanIndex_Type()
)
gw4t2ChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gw4t2ChanIndex.setStatus("current")


class _Gw4t2ChanName_Type(DisplayString):
    """Custom type gw4t2ChanName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gw4t2ChanName_Type.__name__ = "DisplayString"
_Gw4t2ChanName_Object = MibTableColumn
gw4t2ChanName = _Gw4t2ChanName_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 3, 2, 1, 2),
    _Gw4t2ChanName_Type()
)
gw4t2ChanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ChanName.setStatus("current")
_Gw4t2ChanState_Type = Tgw4t2ChanState
_Gw4t2ChanState_Object = MibTableColumn
gw4t2ChanState = _Gw4t2ChanState_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 3, 2, 1, 3),
    _Gw4t2ChanState_Type()
)
gw4t2ChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ChanState.setStatus("current")
_Gw4t2ifCounters_ObjectIdentity = ObjectIdentity
gw4t2ifCounters = _Gw4t2ifCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4)
)
_Gw4t2ifCounterNumber_Type = Integer32
_Gw4t2ifCounterNumber_Object = MibScalar
gw4t2ifCounterNumber = _Gw4t2ifCounterNumber_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 1),
    _Gw4t2ifCounterNumber_Type()
)
gw4t2ifCounterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterNumber.setStatus("current")
_Gw4t2ifCounterTable_Object = MibTable
gw4t2ifCounterTable = _Gw4t2ifCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    gw4t2ifCounterTable.setStatus("current")
_Gw4t2ifCounterEntry_Object = MibTableRow
gw4t2ifCounterEntry = _Gw4t2ifCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1)
)
gw4t2ifCounterEntry.setIndexNames(
    (0, "GW4T2-MIB", "gw4t2ifCounterIndex"),
)
if mibBuilder.loadTexts:
    gw4t2ifCounterEntry.setStatus("current")


class _Gw4t2ifCounterIndex_Type(Integer32):
    """Custom type gw4t2ifCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gw4t2ifCounterIndex_Type.__name__ = "Integer32"
_Gw4t2ifCounterIndex_Object = MibTableColumn
gw4t2ifCounterIndex = _Gw4t2ifCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 1),
    _Gw4t2ifCounterIndex_Type()
)
gw4t2ifCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gw4t2ifCounterIndex.setStatus("current")


class _Gw4t2ifCounterDescr_Type(DisplayString):
    """Custom type gw4t2ifCounterDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gw4t2ifCounterDescr_Type.__name__ = "DisplayString"
_Gw4t2ifCounterDescr_Object = MibTableColumn
gw4t2ifCounterDescr = _Gw4t2ifCounterDescr_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 2),
    _Gw4t2ifCounterDescr_Type()
)
gw4t2ifCounterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterDescr.setStatus("current")


class _Gw4t2ifCounterName_Type(DisplayString):
    """Custom type gw4t2ifCounterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gw4t2ifCounterName_Type.__name__ = "DisplayString"
_Gw4t2ifCounterName_Object = MibTableColumn
gw4t2ifCounterName = _Gw4t2ifCounterName_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 3),
    _Gw4t2ifCounterName_Type()
)
gw4t2ifCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterName.setStatus("current")
_Gw4t2ifCounterInOctets_Type = Counter64
_Gw4t2ifCounterInOctets_Object = MibTableColumn
gw4t2ifCounterInOctets = _Gw4t2ifCounterInOctets_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 4),
    _Gw4t2ifCounterInOctets_Type()
)
gw4t2ifCounterInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterInOctets.setStatus("current")
_Gw4t2ifCounterInUcastPkts_Type = Counter64
_Gw4t2ifCounterInUcastPkts_Object = MibTableColumn
gw4t2ifCounterInUcastPkts = _Gw4t2ifCounterInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 5),
    _Gw4t2ifCounterInUcastPkts_Type()
)
gw4t2ifCounterInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterInUcastPkts.setStatus("current")
_Gw4t2ifCounterInDiscards_Type = Counter64
_Gw4t2ifCounterInDiscards_Object = MibTableColumn
gw4t2ifCounterInDiscards = _Gw4t2ifCounterInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 6),
    _Gw4t2ifCounterInDiscards_Type()
)
gw4t2ifCounterInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterInDiscards.setStatus("current")
_Gw4t2ifCounterInErrors_Type = Counter64
_Gw4t2ifCounterInErrors_Object = MibTableColumn
gw4t2ifCounterInErrors = _Gw4t2ifCounterInErrors_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 7),
    _Gw4t2ifCounterInErrors_Type()
)
gw4t2ifCounterInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterInErrors.setStatus("current")
_Gw4t2ifCounterOutOctets_Type = Counter64
_Gw4t2ifCounterOutOctets_Object = MibTableColumn
gw4t2ifCounterOutOctets = _Gw4t2ifCounterOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 8),
    _Gw4t2ifCounterOutOctets_Type()
)
gw4t2ifCounterOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterOutOctets.setStatus("current")
_Gw4t2ifCounterOutUcastPkts_Type = Counter64
_Gw4t2ifCounterOutUcastPkts_Object = MibTableColumn
gw4t2ifCounterOutUcastPkts = _Gw4t2ifCounterOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 9),
    _Gw4t2ifCounterOutUcastPkts_Type()
)
gw4t2ifCounterOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterOutUcastPkts.setStatus("current")
_Gw4t2ifCounterOutDiscards_Type = Counter64
_Gw4t2ifCounterOutDiscards_Object = MibTableColumn
gw4t2ifCounterOutDiscards = _Gw4t2ifCounterOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 10),
    _Gw4t2ifCounterOutDiscards_Type()
)
gw4t2ifCounterOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterOutDiscards.setStatus("current")
_Gw4t2ifCounterOutErrors_Type = Counter64
_Gw4t2ifCounterOutErrors_Object = MibTableColumn
gw4t2ifCounterOutErrors = _Gw4t2ifCounterOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 4, 2, 1, 11),
    _Gw4t2ifCounterOutErrors_Type()
)
gw4t2ifCounterOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2ifCounterOutErrors.setStatus("current")
_Gw4t2sipAccount_ObjectIdentity = ObjectIdentity
gw4t2sipAccount = _Gw4t2sipAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 5)
)
_Gw4t2sipAccountNumber_Type = Integer32
_Gw4t2sipAccountNumber_Object = MibScalar
gw4t2sipAccountNumber = _Gw4t2sipAccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 5, 1),
    _Gw4t2sipAccountNumber_Type()
)
gw4t2sipAccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2sipAccountNumber.setStatus("current")
_Gw4t2sipAccountTable_Object = MibTable
gw4t2sipAccountTable = _Gw4t2sipAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    gw4t2sipAccountTable.setStatus("current")
_Gw4t2sipAccountEntry_Object = MibTableRow
gw4t2sipAccountEntry = _Gw4t2sipAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 5, 2, 1)
)
gw4t2sipAccountEntry.setIndexNames(
    (0, "GW4T2-MIB", "gw4t2sipAccountIndex"),
)
if mibBuilder.loadTexts:
    gw4t2sipAccountEntry.setStatus("current")


class _Gw4t2sipAccountIndex_Type(Integer32):
    """Custom type gw4t2sipAccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gw4t2sipAccountIndex_Type.__name__ = "Integer32"
_Gw4t2sipAccountIndex_Object = MibTableColumn
gw4t2sipAccountIndex = _Gw4t2sipAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 5, 2, 1, 1),
    _Gw4t2sipAccountIndex_Type()
)
gw4t2sipAccountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gw4t2sipAccountIndex.setStatus("current")
_Gw4t2sipAccountStatus_Type = Tgw4t2sipAccountStatus
_Gw4t2sipAccountStatus_Object = MibTableColumn
gw4t2sipAccountStatus = _Gw4t2sipAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 10, 3, 1, 5, 2, 1, 2),
    _Gw4t2sipAccountStatus_Type()
)
gw4t2sipAccountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gw4t2sipAccountStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GW4T2-MIB",
    **{"Tgw4t2ChanState": Tgw4t2ChanState,
       "Tgw4t2sipAccountStatus": Tgw4t2sipAccountStatus,
       "gatewaygw4t2": gatewaygw4t2,
       "gw4t2": gw4t2,
       "gw4t2Version": gw4t2Version,
       "gw4t2VersionString": gw4t2VersionString,
       "gw4t2Status": gw4t2Status,
       "gw4t2GlobalStatus": gw4t2GlobalStatus,
       "gw4t2Autotests": gw4t2Autotests,
       "gw4t2Channels": gw4t2Channels,
       "gw4t2NumChannels": gw4t2NumChannels,
       "gw4t2ChanTable": gw4t2ChanTable,
       "gw4t2ChanEntry": gw4t2ChanEntry,
       "gw4t2ChanIndex": gw4t2ChanIndex,
       "gw4t2ChanName": gw4t2ChanName,
       "gw4t2ChanState": gw4t2ChanState,
       "gw4t2ifCounters": gw4t2ifCounters,
       "gw4t2ifCounterNumber": gw4t2ifCounterNumber,
       "gw4t2ifCounterTable": gw4t2ifCounterTable,
       "gw4t2ifCounterEntry": gw4t2ifCounterEntry,
       "gw4t2ifCounterIndex": gw4t2ifCounterIndex,
       "gw4t2ifCounterDescr": gw4t2ifCounterDescr,
       "gw4t2ifCounterName": gw4t2ifCounterName,
       "gw4t2ifCounterInOctets": gw4t2ifCounterInOctets,
       "gw4t2ifCounterInUcastPkts": gw4t2ifCounterInUcastPkts,
       "gw4t2ifCounterInDiscards": gw4t2ifCounterInDiscards,
       "gw4t2ifCounterInErrors": gw4t2ifCounterInErrors,
       "gw4t2ifCounterOutOctets": gw4t2ifCounterOutOctets,
       "gw4t2ifCounterOutUcastPkts": gw4t2ifCounterOutUcastPkts,
       "gw4t2ifCounterOutDiscards": gw4t2ifCounterOutDiscards,
       "gw4t2ifCounterOutErrors": gw4t2ifCounterOutErrors,
       "gw4t2sipAccount": gw4t2sipAccount,
       "gw4t2sipAccountNumber": gw4t2sipAccountNumber,
       "gw4t2sipAccountTable": gw4t2sipAccountTable,
       "gw4t2sipAccountEntry": gw4t2sipAccountEntry,
       "gw4t2sipAccountIndex": gw4t2sipAccountIndex,
       "gw4t2sipAccountStatus": gw4t2sipAccountStatus}
)
