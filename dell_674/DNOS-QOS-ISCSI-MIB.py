# SNMP MIB module (DNOS-QOS-ISCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DNOS-QOS-ISCSI-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:25:39 2025
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

(fastPathQOS,) = mibBuilder.importSymbols(
    "DNOS-QOS-MIB",
    "fastPathQOS")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathIscsiFlowAcceleration = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    fastPathIscsiFlowAcceleration.setRevisions(
        ("2011-01-26 00:00",
         "2009-04-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QosType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vpt", 0),
          ("dscp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AgentIscsiFlowAccelerationGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentIscsiFlowAccelerationGlobalConfigGroup = _AgentIscsiFlowAccelerationGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1)
)
_AgentIscsiFlowAccelerationEnable_Type = TruthValue
_AgentIscsiFlowAccelerationEnable_Object = MibScalar
agentIscsiFlowAccelerationEnable = _AgentIscsiFlowAccelerationEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 1),
    _AgentIscsiFlowAccelerationEnable_Type()
)
agentIscsiFlowAccelerationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationEnable.setStatus("current")


class _AgentIscsiFlowAccelerationAgingTimeOut_Type(Integer32):
    """Custom type agentIscsiFlowAccelerationAgingTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2592000),
    )


_AgentIscsiFlowAccelerationAgingTimeOut_Type.__name__ = "Integer32"
_AgentIscsiFlowAccelerationAgingTimeOut_Object = MibScalar
agentIscsiFlowAccelerationAgingTimeOut = _AgentIscsiFlowAccelerationAgingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 2),
    _AgentIscsiFlowAccelerationAgingTimeOut_Type()
)
agentIscsiFlowAccelerationAgingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationAgingTimeOut.setStatus("current")
_AgentIscsiFlowAccelerationQosType_Type = QosType
_AgentIscsiFlowAccelerationQosType_Object = MibScalar
agentIscsiFlowAccelerationQosType = _AgentIscsiFlowAccelerationQosType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 3),
    _AgentIscsiFlowAccelerationQosType_Type()
)
agentIscsiFlowAccelerationQosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationQosType.setStatus("current")


class _AgentIscsiFlowAccelerationQosVptValue_Type(Unsigned32):
    """Custom type agentIscsiFlowAccelerationQosVptValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentIscsiFlowAccelerationQosVptValue_Type.__name__ = "Unsigned32"
_AgentIscsiFlowAccelerationQosVptValue_Object = MibScalar
agentIscsiFlowAccelerationQosVptValue = _AgentIscsiFlowAccelerationQosVptValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 4),
    _AgentIscsiFlowAccelerationQosVptValue_Type()
)
agentIscsiFlowAccelerationQosVptValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationQosVptValue.setStatus("current")


class _AgentIscsiFlowAccelerationQosDscpValue_Type(Unsigned32):
    """Custom type agentIscsiFlowAccelerationQosDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AgentIscsiFlowAccelerationQosDscpValue_Type.__name__ = "Unsigned32"
_AgentIscsiFlowAccelerationQosDscpValue_Object = MibScalar
agentIscsiFlowAccelerationQosDscpValue = _AgentIscsiFlowAccelerationQosDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 5),
    _AgentIscsiFlowAccelerationQosDscpValue_Type()
)
agentIscsiFlowAccelerationQosDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationQosDscpValue.setStatus("current")
_AgentIscsiFlowAccelerationQosRemark_Type = TruthValue
_AgentIscsiFlowAccelerationQosRemark_Object = MibScalar
agentIscsiFlowAccelerationQosRemark = _AgentIscsiFlowAccelerationQosRemark_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 6),
    _AgentIscsiFlowAccelerationQosRemark_Type()
)
agentIscsiFlowAccelerationQosRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationQosRemark.setStatus("current")
_AgentIscsiFlowAccelerationCosEnable_Type = TruthValue
_AgentIscsiFlowAccelerationCosEnable_Object = MibScalar
agentIscsiFlowAccelerationCosEnable = _AgentIscsiFlowAccelerationCosEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 7),
    _AgentIscsiFlowAccelerationCosEnable_Type()
)
agentIscsiFlowAccelerationCosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationCosEnable.setStatus("current")
_AgentIscsiFlowAccelerationTargetConfigTable_Object = MibTable
agentIscsiFlowAccelerationTargetConfigTable = _AgentIscsiFlowAccelerationTargetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationTargetConfigTable.setStatus("current")
_AgentIscsiFlowAccelerationTargetConfigEntry_Object = MibTableRow
agentIscsiFlowAccelerationTargetConfigEntry = _AgentIscsiFlowAccelerationTargetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2, 1)
)
agentIscsiFlowAccelerationTargetConfigEntry.setIndexNames(
    (0, "DNOS-QOS-ISCSI-MIB", "agentIscsiFlowAccelerationTargetConfigTcpPort"),
    (0, "DNOS-QOS-ISCSI-MIB", "agentIscsiFlowAccelerationTargetConfigAddr"),
)
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationTargetConfigEntry.setStatus("current")
_AgentIscsiFlowAccelerationTargetConfigTcpPort_Type = Unsigned32
_AgentIscsiFlowAccelerationTargetConfigTcpPort_Object = MibTableColumn
agentIscsiFlowAccelerationTargetConfigTcpPort = _AgentIscsiFlowAccelerationTargetConfigTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2, 1, 1),
    _AgentIscsiFlowAccelerationTargetConfigTcpPort_Type()
)
agentIscsiFlowAccelerationTargetConfigTcpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationTargetConfigTcpPort.setStatus("current")
_AgentIscsiFlowAccelerationTargetConfigAddr_Type = IpAddress
_AgentIscsiFlowAccelerationTargetConfigAddr_Object = MibTableColumn
agentIscsiFlowAccelerationTargetConfigAddr = _AgentIscsiFlowAccelerationTargetConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2, 1, 2),
    _AgentIscsiFlowAccelerationTargetConfigAddr_Type()
)
agentIscsiFlowAccelerationTargetConfigAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationTargetConfigAddr.setStatus("current")


class _AgentIscsiFlowAccelerationTargetConfigName_Type(DisplayString):
    """Custom type agentIscsiFlowAccelerationTargetConfigName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_AgentIscsiFlowAccelerationTargetConfigName_Type.__name__ = "DisplayString"
_AgentIscsiFlowAccelerationTargetConfigName_Object = MibTableColumn
agentIscsiFlowAccelerationTargetConfigName = _AgentIscsiFlowAccelerationTargetConfigName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2, 1, 3),
    _AgentIscsiFlowAccelerationTargetConfigName_Type()
)
agentIscsiFlowAccelerationTargetConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationTargetConfigName.setStatus("current")
_AgentIscsiFlowAccelerationTargetConfigStatus_Type = RowStatus
_AgentIscsiFlowAccelerationTargetConfigStatus_Object = MibTableColumn
agentIscsiFlowAccelerationTargetConfigStatus = _AgentIscsiFlowAccelerationTargetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2, 1, 4),
    _AgentIscsiFlowAccelerationTargetConfigStatus_Type()
)
agentIscsiFlowAccelerationTargetConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationTargetConfigStatus.setStatus("current")
_AgentIscsiFlowAccelerationSessionTable_Object = MibTable
agentIscsiFlowAccelerationSessionTable = _AgentIscsiFlowAccelerationSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationSessionTable.setStatus("current")
_AgentIscsiFlowAccelerationSessionEntry_Object = MibTableRow
agentIscsiFlowAccelerationSessionEntry = _AgentIscsiFlowAccelerationSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1)
)
agentIscsiFlowAccelerationSessionEntry.setIndexNames(
    (0, "DNOS-QOS-ISCSI-MIB", "agentIscsiFlowAccelerationSessionIndex"),
)
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationSessionEntry.setStatus("current")
_AgentIscsiFlowAccelerationSessionIndex_Type = Unsigned32
_AgentIscsiFlowAccelerationSessionIndex_Object = MibTableColumn
agentIscsiFlowAccelerationSessionIndex = _AgentIscsiFlowAccelerationSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 1),
    _AgentIscsiFlowAccelerationSessionIndex_Type()
)
agentIscsiFlowAccelerationSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationSessionIndex.setStatus("current")


class _AgentIscsiFlowAccelerationTargetName_Type(DisplayString):
    """Custom type agentIscsiFlowAccelerationTargetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_AgentIscsiFlowAccelerationTargetName_Type.__name__ = "DisplayString"
_AgentIscsiFlowAccelerationTargetName_Object = MibTableColumn
agentIscsiFlowAccelerationTargetName = _AgentIscsiFlowAccelerationTargetName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 2),
    _AgentIscsiFlowAccelerationTargetName_Type()
)
agentIscsiFlowAccelerationTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationTargetName.setStatus("current")


class _AgentIscsiFlowAccelerationInitiatorName_Type(DisplayString):
    """Custom type agentIscsiFlowAccelerationInitiatorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_AgentIscsiFlowAccelerationInitiatorName_Type.__name__ = "DisplayString"
_AgentIscsiFlowAccelerationInitiatorName_Object = MibTableColumn
agentIscsiFlowAccelerationInitiatorName = _AgentIscsiFlowAccelerationInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 3),
    _AgentIscsiFlowAccelerationInitiatorName_Type()
)
agentIscsiFlowAccelerationInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationInitiatorName.setStatus("current")


class _AgentIscsiFlowAccelerationSessionISID_Type(OctetString):
    """Custom type agentIscsiFlowAccelerationSessionISID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_AgentIscsiFlowAccelerationSessionISID_Type.__name__ = "OctetString"
_AgentIscsiFlowAccelerationSessionISID_Object = MibTableColumn
agentIscsiFlowAccelerationSessionISID = _AgentIscsiFlowAccelerationSessionISID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 4),
    _AgentIscsiFlowAccelerationSessionISID_Type()
)
agentIscsiFlowAccelerationSessionISID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationSessionISID.setStatus("current")
_AgentIscsiFlowAccelerationSessAgingTime_Type = Unsigned32
_AgentIscsiFlowAccelerationSessAgingTime_Object = MibTableColumn
agentIscsiFlowAccelerationSessAgingTime = _AgentIscsiFlowAccelerationSessAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 5),
    _AgentIscsiFlowAccelerationSessAgingTime_Type()
)
agentIscsiFlowAccelerationSessAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationSessAgingTime.setStatus("current")
_AgentIscsiFlowAccelerationSessionUpTime_Type = Unsigned32
_AgentIscsiFlowAccelerationSessionUpTime_Object = MibTableColumn
agentIscsiFlowAccelerationSessionUpTime = _AgentIscsiFlowAccelerationSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 6),
    _AgentIscsiFlowAccelerationSessionUpTime_Type()
)
agentIscsiFlowAccelerationSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationSessionUpTime.setStatus("current")
_AgentIscsiFlowAccelerationConnectionTable_Object = MibTable
agentIscsiFlowAccelerationConnectionTable = _AgentIscsiFlowAccelerationConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationConnectionTable.setStatus("current")
_AgentIscsiFlowAccelerationConnectionEntry_Object = MibTableRow
agentIscsiFlowAccelerationConnectionEntry = _AgentIscsiFlowAccelerationConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1)
)
agentIscsiFlowAccelerationConnectionEntry.setIndexNames(
    (0, "DNOS-QOS-ISCSI-MIB", "agentIscsiFlowAccelerationConnectionIndex"),
)
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationConnectionEntry.setStatus("current")
_AgentIscsiFlowAccelerationConnectionIndex_Type = Unsigned32
_AgentIscsiFlowAccelerationConnectionIndex_Object = MibTableColumn
agentIscsiFlowAccelerationConnectionIndex = _AgentIscsiFlowAccelerationConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 1),
    _AgentIscsiFlowAccelerationConnectionIndex_Type()
)
agentIscsiFlowAccelerationConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationConnectionIndex.setStatus("current")
_AgentIscsiFlowAccelerationConnectionTargetAddr_Type = IpAddress
_AgentIscsiFlowAccelerationConnectionTargetAddr_Object = MibTableColumn
agentIscsiFlowAccelerationConnectionTargetAddr = _AgentIscsiFlowAccelerationConnectionTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 2),
    _AgentIscsiFlowAccelerationConnectionTargetAddr_Type()
)
agentIscsiFlowAccelerationConnectionTargetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationConnectionTargetAddr.setStatus("current")
_AgentIscsiFlowAccelerationConnectionTargetPort_Type = Unsigned32
_AgentIscsiFlowAccelerationConnectionTargetPort_Object = MibTableColumn
agentIscsiFlowAccelerationConnectionTargetPort = _AgentIscsiFlowAccelerationConnectionTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 3),
    _AgentIscsiFlowAccelerationConnectionTargetPort_Type()
)
agentIscsiFlowAccelerationConnectionTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationConnectionTargetPort.setStatus("current")
_AgentIscsiFlowAccelerationConnectionInitiatorAddr_Type = IpAddress
_AgentIscsiFlowAccelerationConnectionInitiatorAddr_Object = MibTableColumn
agentIscsiFlowAccelerationConnectionInitiatorAddr = _AgentIscsiFlowAccelerationConnectionInitiatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 4),
    _AgentIscsiFlowAccelerationConnectionInitiatorAddr_Type()
)
agentIscsiFlowAccelerationConnectionInitiatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationConnectionInitiatorAddr.setStatus("current")
_AgentIscsiFlowAccelerationConnectionInitiatorPort_Type = Unsigned32
_AgentIscsiFlowAccelerationConnectionInitiatorPort_Object = MibTableColumn
agentIscsiFlowAccelerationConnectionInitiatorPort = _AgentIscsiFlowAccelerationConnectionInitiatorPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 5),
    _AgentIscsiFlowAccelerationConnectionInitiatorPort_Type()
)
agentIscsiFlowAccelerationConnectionInitiatorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationConnectionInitiatorPort.setStatus("current")
_AgentIscsiFlowAccelerationConnectionCID_Type = Unsigned32
_AgentIscsiFlowAccelerationConnectionCID_Object = MibTableColumn
agentIscsiFlowAccelerationConnectionCID = _AgentIscsiFlowAccelerationConnectionCID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 6),
    _AgentIscsiFlowAccelerationConnectionCID_Type()
)
agentIscsiFlowAccelerationConnectionCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationConnectionCID.setStatus("current")
_AgentIscsiFlowAccelerationConnectionSessionIndex_Type = Unsigned32
_AgentIscsiFlowAccelerationConnectionSessionIndex_Object = MibTableColumn
agentIscsiFlowAccelerationConnectionSessionIndex = _AgentIscsiFlowAccelerationConnectionSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 7),
    _AgentIscsiFlowAccelerationConnectionSessionIndex_Type()
)
agentIscsiFlowAccelerationConnectionSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIscsiFlowAccelerationConnectionSessionIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-QOS-ISCSI-MIB",
    **{"QosType": QosType,
       "fastPathIscsiFlowAcceleration": fastPathIscsiFlowAcceleration,
       "agentIscsiFlowAccelerationGlobalConfigGroup": agentIscsiFlowAccelerationGlobalConfigGroup,
       "agentIscsiFlowAccelerationEnable": agentIscsiFlowAccelerationEnable,
       "agentIscsiFlowAccelerationAgingTimeOut": agentIscsiFlowAccelerationAgingTimeOut,
       "agentIscsiFlowAccelerationQosType": agentIscsiFlowAccelerationQosType,
       "agentIscsiFlowAccelerationQosVptValue": agentIscsiFlowAccelerationQosVptValue,
       "agentIscsiFlowAccelerationQosDscpValue": agentIscsiFlowAccelerationQosDscpValue,
       "agentIscsiFlowAccelerationQosRemark": agentIscsiFlowAccelerationQosRemark,
       "agentIscsiFlowAccelerationCosEnable": agentIscsiFlowAccelerationCosEnable,
       "agentIscsiFlowAccelerationTargetConfigTable": agentIscsiFlowAccelerationTargetConfigTable,
       "agentIscsiFlowAccelerationTargetConfigEntry": agentIscsiFlowAccelerationTargetConfigEntry,
       "agentIscsiFlowAccelerationTargetConfigTcpPort": agentIscsiFlowAccelerationTargetConfigTcpPort,
       "agentIscsiFlowAccelerationTargetConfigAddr": agentIscsiFlowAccelerationTargetConfigAddr,
       "agentIscsiFlowAccelerationTargetConfigName": agentIscsiFlowAccelerationTargetConfigName,
       "agentIscsiFlowAccelerationTargetConfigStatus": agentIscsiFlowAccelerationTargetConfigStatus,
       "agentIscsiFlowAccelerationSessionTable": agentIscsiFlowAccelerationSessionTable,
       "agentIscsiFlowAccelerationSessionEntry": agentIscsiFlowAccelerationSessionEntry,
       "agentIscsiFlowAccelerationSessionIndex": agentIscsiFlowAccelerationSessionIndex,
       "agentIscsiFlowAccelerationTargetName": agentIscsiFlowAccelerationTargetName,
       "agentIscsiFlowAccelerationInitiatorName": agentIscsiFlowAccelerationInitiatorName,
       "agentIscsiFlowAccelerationSessionISID": agentIscsiFlowAccelerationSessionISID,
       "agentIscsiFlowAccelerationSessAgingTime": agentIscsiFlowAccelerationSessAgingTime,
       "agentIscsiFlowAccelerationSessionUpTime": agentIscsiFlowAccelerationSessionUpTime,
       "agentIscsiFlowAccelerationConnectionTable": agentIscsiFlowAccelerationConnectionTable,
       "agentIscsiFlowAccelerationConnectionEntry": agentIscsiFlowAccelerationConnectionEntry,
       "agentIscsiFlowAccelerationConnectionIndex": agentIscsiFlowAccelerationConnectionIndex,
       "agentIscsiFlowAccelerationConnectionTargetAddr": agentIscsiFlowAccelerationConnectionTargetAddr,
       "agentIscsiFlowAccelerationConnectionTargetPort": agentIscsiFlowAccelerationConnectionTargetPort,
       "agentIscsiFlowAccelerationConnectionInitiatorAddr": agentIscsiFlowAccelerationConnectionInitiatorAddr,
       "agentIscsiFlowAccelerationConnectionInitiatorPort": agentIscsiFlowAccelerationConnectionInitiatorPort,
       "agentIscsiFlowAccelerationConnectionCID": agentIscsiFlowAccelerationConnectionCID,
       "agentIscsiFlowAccelerationConnectionSessionIndex": agentIscsiFlowAccelerationConnectionSessionIndex}
)
