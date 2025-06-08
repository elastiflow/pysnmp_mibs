# SNMP MIB module (TN-SAS-SERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-SAS-SERV-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:06:37 2025
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

(tnSapBaseInfoEntry,
 tnSapBaseStatsEntry) = mibBuilder.importSymbols(
    "TN-SAP-MIB",
    "tnSapBaseInfoEntry",
    "tnSapBaseStatsEntry")

(tnSvcBaseInfoEntry,) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "tnSvcBaseInfoEntry")

(tnSASModules,
 tnSASObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSASModules",
    "tnSASObjs")


# MODULE-IDENTITY

tnSASServicesMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tnSASServicesMIBModule.setRevisions(
        ("1912-12-05 00:00",
         "1912-08-22 00:00",
         "1909-07-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TSapIngressAggrMeterBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(4, 2146959),
    )



# MIB Managed Objects in the order of their OIDs

_TnSASServObjs_ObjectIdentity = ObjectIdentity
tnSASServObjs = _TnSASServObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8)
)
_TnSASSapObjs_ObjectIdentity = ObjectIdentity
tnSASSapObjs = _TnSASSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1)
)
_TnSapBaseStatsExtnTable_Object = MibTable
tnSapBaseStatsExtnTable = _TnSapBaseStatsExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    tnSapBaseStatsExtnTable.setStatus("current")
_TnSapBaseStatsExtnEntry_Object = MibTableRow
tnSapBaseStatsExtnEntry = _TnSapBaseStatsExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnSapBaseStatsExtnEntry.setStatus("current")
_TnSapBaseStatsQosClassifiersUsed_Type = Unsigned32
_TnSapBaseStatsQosClassifiersUsed_Object = MibTableColumn
tnSapBaseStatsQosClassifiersUsed = _TnSapBaseStatsQosClassifiersUsed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1, 1),
    _TnSapBaseStatsQosClassifiersUsed_Type()
)
tnSapBaseStatsQosClassifiersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsQosClassifiersUsed.setStatus("current")
_TnSapBaseStatsQosMetersUsed_Type = Unsigned32
_TnSapBaseStatsQosMetersUsed_Object = MibTableColumn
tnSapBaseStatsQosMetersUsed = _TnSapBaseStatsQosMetersUsed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1, 2),
    _TnSapBaseStatsQosMetersUsed_Type()
)
tnSapBaseStatsQosMetersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsQosMetersUsed.setStatus("current")
_TnSapBaseStatsIngressForwardedPackets_Type = Counter64
_TnSapBaseStatsIngressForwardedPackets_Object = MibTableColumn
tnSapBaseStatsIngressForwardedPackets = _TnSapBaseStatsIngressForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1, 3),
    _TnSapBaseStatsIngressForwardedPackets_Type()
)
tnSapBaseStatsIngressForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressForwardedPackets.setStatus("current")
_TnSapBaseStatsIngressForwardedOctets_Type = Counter64
_TnSapBaseStatsIngressForwardedOctets_Object = MibTableColumn
tnSapBaseStatsIngressForwardedOctets = _TnSapBaseStatsIngressForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1, 4),
    _TnSapBaseStatsIngressForwardedOctets_Type()
)
tnSapBaseStatsIngressForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressForwardedOctets.setStatus("current")
_TnSapBaseStatsEgressForwardedPackets_Type = Counter64
_TnSapBaseStatsEgressForwardedPackets_Object = MibTableColumn
tnSapBaseStatsEgressForwardedPackets = _TnSapBaseStatsEgressForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1, 5),
    _TnSapBaseStatsEgressForwardedPackets_Type()
)
tnSapBaseStatsEgressForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsEgressForwardedPackets.setStatus("current")
_TnSapBaseStatsEgressForwardedOctets_Type = Counter64
_TnSapBaseStatsEgressForwardedOctets_Object = MibTableColumn
tnSapBaseStatsEgressForwardedOctets = _TnSapBaseStatsEgressForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1, 6),
    _TnSapBaseStatsEgressForwardedOctets_Type()
)
tnSapBaseStatsEgressForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsEgressForwardedOctets.setStatus("current")
_TnSapBaseStatsIngressExtraTagDroppedPackets_Type = Counter64
_TnSapBaseStatsIngressExtraTagDroppedPackets_Object = MibTableColumn
tnSapBaseStatsIngressExtraTagDroppedPackets = _TnSapBaseStatsIngressExtraTagDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1, 7),
    _TnSapBaseStatsIngressExtraTagDroppedPackets_Type()
)
tnSapBaseStatsIngressExtraTagDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressExtraTagDroppedPackets.setStatus("current")
_TnSapBaseStatsIngressExtraTagDroppedOctets_Type = Counter64
_TnSapBaseStatsIngressExtraTagDroppedOctets_Object = MibTableColumn
tnSapBaseStatsIngressExtraTagDroppedOctets = _TnSapBaseStatsIngressExtraTagDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1, 8),
    _TnSapBaseStatsIngressExtraTagDroppedOctets_Type()
)
tnSapBaseStatsIngressExtraTagDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressExtraTagDroppedOctets.setStatus("current")
_TnSapBaseStatsIngressDroppedPackets_Type = Counter64
_TnSapBaseStatsIngressDroppedPackets_Object = MibTableColumn
tnSapBaseStatsIngressDroppedPackets = _TnSapBaseStatsIngressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1, 9),
    _TnSapBaseStatsIngressDroppedPackets_Type()
)
tnSapBaseStatsIngressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressDroppedPackets.setStatus("current")
_TnSapBaseStatsIngressDroppedOctets_Type = Counter64
_TnSapBaseStatsIngressDroppedOctets_Object = MibTableColumn
tnSapBaseStatsIngressDroppedOctets = _TnSapBaseStatsIngressDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 1, 1, 10),
    _TnSapBaseStatsIngressDroppedOctets_Type()
)
tnSapBaseStatsIngressDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapBaseStatsIngressDroppedOctets.setStatus("current")
_TnSapBaseInfoExtnTable_Object = MibTable
tnSapBaseInfoExtnTable = _TnSapBaseInfoExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    tnSapBaseInfoExtnTable.setStatus("current")
_TnSapBaseInfoExtnEntry_Object = MibTableRow
tnSapBaseInfoExtnEntry = _TnSapBaseInfoExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnSapBaseInfoExtnEntry.setStatus("current")


class _TnSapBaseInfoEgressStatsPktsMode_Type(TruthValue):
    """Custom type tnSapBaseInfoEgressStatsPktsMode based on TruthValue"""
    defaultValue = 2


_TnSapBaseInfoEgressStatsPktsMode_Type.__name__ = "TruthValue"
_TnSapBaseInfoEgressStatsPktsMode_Object = MibTableColumn
tnSapBaseInfoEgressStatsPktsMode = _TnSapBaseInfoEgressStatsPktsMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1, 1),
    _TnSapBaseInfoEgressStatsPktsMode_Type()
)
tnSapBaseInfoEgressStatsPktsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapBaseInfoEgressStatsPktsMode.setStatus("current")


class _TnSapBaseInfoIngressCounterMode_Type(Integer32):
    """Custom type tnSapBaseInfoIngressCounterMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("octet", 2))
    )


_TnSapBaseInfoIngressCounterMode_Type.__name__ = "Integer32"
_TnSapBaseInfoIngressCounterMode_Object = MibTableColumn
tnSapBaseInfoIngressCounterMode = _TnSapBaseInfoIngressCounterMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1, 2),
    _TnSapBaseInfoIngressCounterMode_Type()
)
tnSapBaseInfoIngressCounterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapBaseInfoIngressCounterMode.setStatus("current")


class _TnSapBaseInfoIngressAggregateMeterRate_Type(Integer32):
    """Custom type tnSapBaseInfoIngressAggregateMeterRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 20000000),
    )


_TnSapBaseInfoIngressAggregateMeterRate_Type.__name__ = "Integer32"
_TnSapBaseInfoIngressAggregateMeterRate_Object = MibTableColumn
tnSapBaseInfoIngressAggregateMeterRate = _TnSapBaseInfoIngressAggregateMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1, 3),
    _TnSapBaseInfoIngressAggregateMeterRate_Type()
)
tnSapBaseInfoIngressAggregateMeterRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapBaseInfoIngressAggregateMeterRate.setStatus("current")


class _TnSapBaseInfoIngressAggregateMeterBurst_Type(TSapIngressAggrMeterBurstSize):
    """Custom type tnSapBaseInfoIngressAggregateMeterBurst based on TSapIngressAggrMeterBurstSize"""
    defaultValue = -1


_TnSapBaseInfoIngressAggregateMeterBurst_Type.__name__ = "TSapIngressAggrMeterBurstSize"
_TnSapBaseInfoIngressAggregateMeterBurst_Object = MibTableColumn
tnSapBaseInfoIngressAggregateMeterBurst = _TnSapBaseInfoIngressAggregateMeterBurst_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1, 4),
    _TnSapBaseInfoIngressAggregateMeterBurst_Type()
)
tnSapBaseInfoIngressAggregateMeterBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapBaseInfoIngressAggregateMeterBurst.setStatus("current")


class _TnSapBaseInfoIngressWithAggregateMeter_Type(TruthValue):
    """Custom type tnSapBaseInfoIngressWithAggregateMeter based on TruthValue"""
    defaultValue = 2


_TnSapBaseInfoIngressWithAggregateMeter_Type.__name__ = "TruthValue"
_TnSapBaseInfoIngressWithAggregateMeter_Object = MibTableColumn
tnSapBaseInfoIngressWithAggregateMeter = _TnSapBaseInfoIngressWithAggregateMeter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1, 5),
    _TnSapBaseInfoIngressWithAggregateMeter_Type()
)
tnSapBaseInfoIngressWithAggregateMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapBaseInfoIngressWithAggregateMeter.setStatus("current")


class _TnSapBaseInfoIngressExtraTagDropCount_Type(TruthValue):
    """Custom type tnSapBaseInfoIngressExtraTagDropCount based on TruthValue"""
    defaultValue = 2


_TnSapBaseInfoIngressExtraTagDropCount_Type.__name__ = "TruthValue"
_TnSapBaseInfoIngressExtraTagDropCount_Object = MibTableColumn
tnSapBaseInfoIngressExtraTagDropCount = _TnSapBaseInfoIngressExtraTagDropCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1, 6),
    _TnSapBaseInfoIngressExtraTagDropCount_Type()
)
tnSapBaseInfoIngressExtraTagDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapBaseInfoIngressExtraTagDropCount.setStatus("current")


class _TnSapBaseInfoEgressStatsEnable_Type(TruthValue):
    """Custom type tnSapBaseInfoEgressStatsEnable based on TruthValue"""
    defaultValue = 2


_TnSapBaseInfoEgressStatsEnable_Type.__name__ = "TruthValue"
_TnSapBaseInfoEgressStatsEnable_Object = MibTableColumn
tnSapBaseInfoEgressStatsEnable = _TnSapBaseInfoEgressStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1, 7),
    _TnSapBaseInfoEgressStatsEnable_Type()
)
tnSapBaseInfoEgressStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapBaseInfoEgressStatsEnable.setStatus("current")


class _TnSapBaseInfoIngressStatsEnable_Type(TruthValue):
    """Custom type tnSapBaseInfoIngressStatsEnable based on TruthValue"""
    defaultValue = 2


_TnSapBaseInfoIngressStatsEnable_Type.__name__ = "TruthValue"
_TnSapBaseInfoIngressStatsEnable_Object = MibTableColumn
tnSapBaseInfoIngressStatsEnable = _TnSapBaseInfoIngressStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1, 8),
    _TnSapBaseInfoIngressStatsEnable_Type()
)
tnSapBaseInfoIngressStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapBaseInfoIngressStatsEnable.setStatus("current")


class _TnSapBaseInfoIngressCounterType_Type(Integer32):
    """Custom type tnSapBaseInfoIngressCounterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-out-profile-count", 1),
          ("forward-drop-count", 2))
    )


_TnSapBaseInfoIngressCounterType_Type.__name__ = "Integer32"
_TnSapBaseInfoIngressCounterType_Object = MibTableColumn
tnSapBaseInfoIngressCounterType = _TnSapBaseInfoIngressCounterType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1, 9),
    _TnSapBaseInfoIngressCounterType_Type()
)
tnSapBaseInfoIngressCounterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapBaseInfoIngressCounterType.setStatus("current")


class _TnSapBaseInfoEthRingShgEnable_Type(TruthValue):
    """Custom type tnSapBaseInfoEthRingShgEnable based on TruthValue"""
    defaultValue = 2


_TnSapBaseInfoEthRingShgEnable_Type.__name__ = "TruthValue"
_TnSapBaseInfoEthRingShgEnable_Object = MibTableColumn
tnSapBaseInfoEthRingShgEnable = _TnSapBaseInfoEthRingShgEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 1, 2, 1, 11),
    _TnSapBaseInfoEthRingShgEnable_Type()
)
tnSapBaseInfoEthRingShgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapBaseInfoEthRingShgEnable.setStatus("current")
_TnSASSvcObjs_ObjectIdentity = ObjectIdentity
tnSASSvcObjs = _TnSASSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 2)
)
_TnSvcBaseInfoExtnTable_Object = MibTable
tnSvcBaseInfoExtnTable = _TnSvcBaseInfoExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    tnSvcBaseInfoExtnTable.setStatus("current")
_TnSvcBaseInfoExtnEntry_Object = MibTableRow
tnSvcBaseInfoExtnEntry = _TnSvcBaseInfoExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnSvcBaseInfoExtnEntry.setStatus("current")


class _TnSvcMtuCheck_Type(TruthValue):
    """Custom type tnSvcMtuCheck based on TruthValue"""
    defaultValue = 1


_TnSvcMtuCheck_Type.__name__ = "TruthValue"
_TnSvcMtuCheck_Object = MibTableColumn
tnSvcMtuCheck = _TnSvcMtuCheck_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 2, 1, 1, 1),
    _TnSvcMtuCheck_Type()
)
tnSvcMtuCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcMtuCheck.setStatus("current")


class _TnSvcSapType_Type(Integer32):
    """Custom type tnSvcSapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("null-star", 1),
          ("dot1q", 2),
          ("dot1q-preserve", 3),
          ("any", 4))
    )


_TnSvcSapType_Type.__name__ = "Integer32"
_TnSvcSapType_Object = MibTableColumn
tnSvcSapType = _TnSvcSapType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 2, 1, 1, 2),
    _TnSvcSapType_Type()
)
tnSvcSapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcSapType.setStatus("current")


class _TnSvcUplinkType_Type(Integer32):
    """Custom type tnSvcUplinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("l2", 1),
          ("mpls", 2))
    )


_TnSvcUplinkType_Type.__name__ = "Integer32"
_TnSvcUplinkType_Object = MibTableColumn
tnSvcUplinkType = _TnSvcUplinkType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 2, 1, 1, 3),
    _TnSvcUplinkType_Type()
)
tnSvcUplinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcUplinkType.setStatus("current")


class _TnSvcCustomerVid_Type(Integer32):
    """Custom type tnSvcCustomerVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnSvcCustomerVid_Type.__name__ = "Integer32"
_TnSvcCustomerVid_Object = MibTableColumn
tnSvcCustomerVid = _TnSvcCustomerVid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 2, 1, 1, 4),
    _TnSvcCustomerVid_Type()
)
tnSvcCustomerVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcCustomerVid.setStatus("current")


class _TnSvcEpipeType_Type(Integer32):
    """Custom type tnSvcEpipeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pbbepipe", 2))
    )


_TnSvcEpipeType_Type.__name__ = "Integer32"
_TnSvcEpipeType_Object = MibTableColumn
tnSvcEpipeType = _TnSvcEpipeType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 2, 1, 1, 5),
    _TnSvcEpipeType_Type()
)
tnSvcEpipeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSvcEpipeType.setStatus("current")
_TnSASSvcScalar1_Type = Unsigned32
_TnSASSvcScalar1_Object = MibScalar
tnSASSvcScalar1 = _TnSASSvcScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 2, 101),
    _TnSASSvcScalar1_Type()
)
tnSASSvcScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASSvcScalar1.setStatus("current")
_TnSASSvcScalar2_Type = Unsigned32
_TnSASSvcScalar2_Object = MibScalar
tnSASSvcScalar2 = _TnSASSvcScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 8, 2, 102),
    _TnSASSvcScalar2_Type()
)
tnSASSvcScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASSvcScalar2.setStatus("current")
tnSapBaseStatsEntry.registerAugmentions(
    ("TN-SAS-SERV-MIB",
     "tnSapBaseStatsExtnEntry")
)
tnSapBaseStatsExtnEntry.setIndexNames(*tnSapBaseStatsEntry.getIndexNames())
tnSapBaseInfoEntry.registerAugmentions(
    ("TN-SAS-SERV-MIB",
     "tnSapBaseInfoExtnEntry")
)
tnSapBaseInfoExtnEntry.setIndexNames(*tnSapBaseInfoEntry.getIndexNames())
tnSvcBaseInfoEntry.registerAugmentions(
    ("TN-SAS-SERV-MIB",
     "tnSvcBaseInfoExtnEntry")
)
tnSvcBaseInfoExtnEntry.setIndexNames(*tnSvcBaseInfoEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SAS-SERV-MIB",
    **{"TSapIngressAggrMeterBurstSize": TSapIngressAggrMeterBurstSize,
       "tnSASServicesMIBModule": tnSASServicesMIBModule,
       "tnSASServObjs": tnSASServObjs,
       "tnSASSapObjs": tnSASSapObjs,
       "tnSapBaseStatsExtnTable": tnSapBaseStatsExtnTable,
       "tnSapBaseStatsExtnEntry": tnSapBaseStatsExtnEntry,
       "tnSapBaseStatsQosClassifiersUsed": tnSapBaseStatsQosClassifiersUsed,
       "tnSapBaseStatsQosMetersUsed": tnSapBaseStatsQosMetersUsed,
       "tnSapBaseStatsIngressForwardedPackets": tnSapBaseStatsIngressForwardedPackets,
       "tnSapBaseStatsIngressForwardedOctets": tnSapBaseStatsIngressForwardedOctets,
       "tnSapBaseStatsEgressForwardedPackets": tnSapBaseStatsEgressForwardedPackets,
       "tnSapBaseStatsEgressForwardedOctets": tnSapBaseStatsEgressForwardedOctets,
       "tnSapBaseStatsIngressExtraTagDroppedPackets": tnSapBaseStatsIngressExtraTagDroppedPackets,
       "tnSapBaseStatsIngressExtraTagDroppedOctets": tnSapBaseStatsIngressExtraTagDroppedOctets,
       "tnSapBaseStatsIngressDroppedPackets": tnSapBaseStatsIngressDroppedPackets,
       "tnSapBaseStatsIngressDroppedOctets": tnSapBaseStatsIngressDroppedOctets,
       "tnSapBaseInfoExtnTable": tnSapBaseInfoExtnTable,
       "tnSapBaseInfoExtnEntry": tnSapBaseInfoExtnEntry,
       "tnSapBaseInfoEgressStatsPktsMode": tnSapBaseInfoEgressStatsPktsMode,
       "tnSapBaseInfoIngressCounterMode": tnSapBaseInfoIngressCounterMode,
       "tnSapBaseInfoIngressAggregateMeterRate": tnSapBaseInfoIngressAggregateMeterRate,
       "tnSapBaseInfoIngressAggregateMeterBurst": tnSapBaseInfoIngressAggregateMeterBurst,
       "tnSapBaseInfoIngressWithAggregateMeter": tnSapBaseInfoIngressWithAggregateMeter,
       "tnSapBaseInfoIngressExtraTagDropCount": tnSapBaseInfoIngressExtraTagDropCount,
       "tnSapBaseInfoEgressStatsEnable": tnSapBaseInfoEgressStatsEnable,
       "tnSapBaseInfoIngressStatsEnable": tnSapBaseInfoIngressStatsEnable,
       "tnSapBaseInfoIngressCounterType": tnSapBaseInfoIngressCounterType,
       "tnSapBaseInfoEthRingShgEnable": tnSapBaseInfoEthRingShgEnable,
       "tnSASSvcObjs": tnSASSvcObjs,
       "tnSvcBaseInfoExtnTable": tnSvcBaseInfoExtnTable,
       "tnSvcBaseInfoExtnEntry": tnSvcBaseInfoExtnEntry,
       "tnSvcMtuCheck": tnSvcMtuCheck,
       "tnSvcSapType": tnSvcSapType,
       "tnSvcUplinkType": tnSvcUplinkType,
       "tnSvcCustomerVid": tnSvcCustomerVid,
       "tnSvcEpipeType": tnSvcEpipeType,
       "tnSASSvcScalar1": tnSASSvcScalar1,
       "tnSASSvcScalar2": tnSASSvcScalar2}
)
