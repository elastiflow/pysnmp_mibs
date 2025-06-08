# SNMP MIB module (RUIJIE-IP-SLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-IP-SLA-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:17 2025
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

(pingCtlOwnerIndex,
 pingCtlTestName) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "pingCtlOwnerIndex",
    "pingCtlTestName")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieRouterQoSMIB,) = mibBuilder.importSymbols(
    "RUIJIE-ROUTER-QOS-MIB",
    "ruijieRouterQoSMIB")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieIpSlaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5)
)
if mibBuilder.loadTexts:
    ruijieIpSlaMIB.setRevisions(
        ("2014-09-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieIpSlaMIBObjects_ObjectIdentity = ObjectIdentity
ruijieIpSlaMIBObjects = _RuijieIpSlaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1)
)
_RuijieIpSlaResultsTable_Object = MibTable
ruijieIpSlaResultsTable = _RuijieIpSlaResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieIpSlaResultsTable.setStatus("current")
_RuijieIpSlaResultsEntry_Object = MibTableRow
ruijieIpSlaResultsEntry = _RuijieIpSlaResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1)
)
ruijieIpSlaResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    ruijieIpSlaResultsEntry.setStatus("current")


class _RuijieIpSlaResultsOperStatus_Type(Integer32):
    """Custom type ruijieIpSlaResultsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("completed", 3))
    )


_RuijieIpSlaResultsOperStatus_Type.__name__ = "Integer32"
_RuijieIpSlaResultsOperStatus_Object = MibTableColumn
ruijieIpSlaResultsOperStatus = _RuijieIpSlaResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 1),
    _RuijieIpSlaResultsOperStatus_Type()
)
ruijieIpSlaResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsOperStatus.setStatus("current")


class _RuijieIpSlaResultsIpTargetAddressType_Type(InetAddressType):
    """Custom type ruijieIpSlaResultsIpTargetAddressType based on InetAddressType"""
    defaultValue = 0


_RuijieIpSlaResultsIpTargetAddressType_Type.__name__ = "InetAddressType"
_RuijieIpSlaResultsIpTargetAddressType_Object = MibTableColumn
ruijieIpSlaResultsIpTargetAddressType = _RuijieIpSlaResultsIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 2),
    _RuijieIpSlaResultsIpTargetAddressType_Type()
)
ruijieIpSlaResultsIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsIpTargetAddressType.setStatus("current")


class _RuijieIpSlaResultsIpTargetAddress_Type(InetAddress):
    """Custom type ruijieIpSlaResultsIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_RuijieIpSlaResultsIpTargetAddress_Type.__name__ = "InetAddress"
_RuijieIpSlaResultsIpTargetAddress_Object = MibTableColumn
ruijieIpSlaResultsIpTargetAddress = _RuijieIpSlaResultsIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 3),
    _RuijieIpSlaResultsIpTargetAddress_Type()
)
ruijieIpSlaResultsIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsIpTargetAddress.setStatus("current")
_RuijieIpSlaResultsMaxRtt_Type = Unsigned32
_RuijieIpSlaResultsMaxRtt_Object = MibTableColumn
ruijieIpSlaResultsMaxRtt = _RuijieIpSlaResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 4),
    _RuijieIpSlaResultsMaxRtt_Type()
)
ruijieIpSlaResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsMaxRtt.setUnits("milliseconds")
_RuijieIpSlaResultsMinRtt_Type = Unsigned32
_RuijieIpSlaResultsMinRtt_Object = MibTableColumn
ruijieIpSlaResultsMinRtt = _RuijieIpSlaResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 5),
    _RuijieIpSlaResultsMinRtt_Type()
)
ruijieIpSlaResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsMinRtt.setUnits("milliseconds")
_RuijieIpSlaResultsAverageRtt_Type = Unsigned32
_RuijieIpSlaResultsAverageRtt_Object = MibTableColumn
ruijieIpSlaResultsAverageRtt = _RuijieIpSlaResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 6),
    _RuijieIpSlaResultsAverageRtt_Type()
)
ruijieIpSlaResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsAverageRtt.setUnits("milliseconds")
_RuijieIpSlaResultsDelayJitter_Type = Unsigned32
_RuijieIpSlaResultsDelayJitter_Object = MibTableColumn
ruijieIpSlaResultsDelayJitter = _RuijieIpSlaResultsDelayJitter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 7),
    _RuijieIpSlaResultsDelayJitter_Type()
)
ruijieIpSlaResultsDelayJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsDelayJitter.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsDelayJitter.setUnits("milliseconds")
_RuijieIpSlaResultsPktsLossRate_Type = Unsigned32
_RuijieIpSlaResultsPktsLossRate_Object = MibTableColumn
ruijieIpSlaResultsPktsLossRate = _RuijieIpSlaResultsPktsLossRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 8),
    _RuijieIpSlaResultsPktsLossRate_Type()
)
ruijieIpSlaResultsPktsLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsPktsLossRate.setStatus("current")
_RuijieIpSlaResultsNetworkAF_Type = Unsigned32
_RuijieIpSlaResultsNetworkAF_Object = MibTableColumn
ruijieIpSlaResultsNetworkAF = _RuijieIpSlaResultsNetworkAF_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 9),
    _RuijieIpSlaResultsNetworkAF_Type()
)
ruijieIpSlaResultsNetworkAF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsNetworkAF.setStatus("current")
_RuijieIpSlaResultsProbeResponses_Type = Gauge32
_RuijieIpSlaResultsProbeResponses_Object = MibTableColumn
ruijieIpSlaResultsProbeResponses = _RuijieIpSlaResultsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 10),
    _RuijieIpSlaResultsProbeResponses_Type()
)
ruijieIpSlaResultsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsProbeResponses.setUnits("responses")
_RuijieIpSlaResultsSentProbes_Type = Gauge32
_RuijieIpSlaResultsSentProbes_Object = MibTableColumn
ruijieIpSlaResultsSentProbes = _RuijieIpSlaResultsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 11),
    _RuijieIpSlaResultsSentProbes_Type()
)
ruijieIpSlaResultsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsSentProbes.setUnits("probes")
_RuijieIpSlaResultsRttSumOfSquares_Type = Unsigned32
_RuijieIpSlaResultsRttSumOfSquares_Object = MibTableColumn
ruijieIpSlaResultsRttSumOfSquares = _RuijieIpSlaResultsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 12),
    _RuijieIpSlaResultsRttSumOfSquares_Type()
)
ruijieIpSlaResultsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsRttSumOfSquares.setUnits("milliseconds")
_RuijieIpSlaResultsLastGoodProbe_Type = DateAndTime
_RuijieIpSlaResultsLastGoodProbe_Object = MibTableColumn
ruijieIpSlaResultsLastGoodProbe = _RuijieIpSlaResultsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 106, 5, 1, 1, 1, 13),
    _RuijieIpSlaResultsLastGoodProbe_Type()
)
ruijieIpSlaResultsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpSlaResultsLastGoodProbe.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-IP-SLA-MIB",
    **{"ruijieIpSlaMIB": ruijieIpSlaMIB,
       "ruijieIpSlaMIBObjects": ruijieIpSlaMIBObjects,
       "ruijieIpSlaResultsTable": ruijieIpSlaResultsTable,
       "ruijieIpSlaResultsEntry": ruijieIpSlaResultsEntry,
       "ruijieIpSlaResultsOperStatus": ruijieIpSlaResultsOperStatus,
       "ruijieIpSlaResultsIpTargetAddressType": ruijieIpSlaResultsIpTargetAddressType,
       "ruijieIpSlaResultsIpTargetAddress": ruijieIpSlaResultsIpTargetAddress,
       "ruijieIpSlaResultsMaxRtt": ruijieIpSlaResultsMaxRtt,
       "ruijieIpSlaResultsMinRtt": ruijieIpSlaResultsMinRtt,
       "ruijieIpSlaResultsAverageRtt": ruijieIpSlaResultsAverageRtt,
       "ruijieIpSlaResultsDelayJitter": ruijieIpSlaResultsDelayJitter,
       "ruijieIpSlaResultsPktsLossRate": ruijieIpSlaResultsPktsLossRate,
       "ruijieIpSlaResultsNetworkAF": ruijieIpSlaResultsNetworkAF,
       "ruijieIpSlaResultsProbeResponses": ruijieIpSlaResultsProbeResponses,
       "ruijieIpSlaResultsSentProbes": ruijieIpSlaResultsSentProbes,
       "ruijieIpSlaResultsRttSumOfSquares": ruijieIpSlaResultsRttSumOfSquares,
       "ruijieIpSlaResultsLastGoodProbe": ruijieIpSlaResultsLastGoodProbe}
)
