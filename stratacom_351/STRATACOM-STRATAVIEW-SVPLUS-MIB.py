# SNMP MIB module (STRATACOM-STRATAVIEW-SVPLUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/STRATACOM-STRATAVIEW-SVPLUS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:11:01 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Active(Integer32):
    """Custom type Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )





class Severity(DisplayString):
    """Custom type Severity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Stratacom_ObjectIdentity = ObjectIdentity
stratacom = _Stratacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351)
)
_Svplus_ObjectIdentity = ObjectIdentity
svplus = _Svplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1)
)
_ControlGroup_ObjectIdentity = ObjectIdentity
controlGroup = _ControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 11)
)


class _DatabaseSampleFreq_Type(Integer32):
    """Custom type databaseSampleFreq based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_DatabaseSampleFreq_Type.__name__ = "Integer32"
_DatabaseSampleFreq_Object = MibScalar
databaseSampleFreq = _DatabaseSampleFreq_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 11, 1),
    _DatabaseSampleFreq_Type()
)
databaseSampleFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseSampleFreq.setStatus("mandatory")
_LogGroup_ObjectIdentity = ObjectIdentity
logGroup = _LogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 12)
)
_CurrentMaxLogIndex_Type = Integer32
_CurrentMaxLogIndex_Object = MibScalar
currentMaxLogIndex = _CurrentMaxLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 1),
    _CurrentMaxLogIndex_Type()
)
currentMaxLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMaxLogIndex.setStatus("mandatory")
_MaintLogTable_Object = MibTable
maintLogTable = _MaintLogTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2)
)
if mibBuilder.loadTexts:
    maintLogTable.setStatus("mandatory")
_MaintLogEntry_Object = MibTableRow
maintLogEntry = _MaintLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1)
)
maintLogEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    maintLogEntry.setStatus("mandatory")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1073741824),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("mandatory")


class _LogNetwork_Type(DisplayString):
    """Custom type logNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LogNetwork_Type.__name__ = "DisplayString"
_LogNetwork_Object = MibTableColumn
logNetwork = _LogNetwork_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 2),
    _LogNetwork_Type()
)
logNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logNetwork.setStatus("mandatory")


class _LogNodeName_Type(DisplayString):
    """Custom type logNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LogNodeName_Type.__name__ = "DisplayString"
_LogNodeName_Object = MibTableColumn
logNodeName = _LogNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 3),
    _LogNodeName_Type()
)
logNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logNodeName.setStatus("mandatory")


class _LogGmtDate_Type(DisplayString):
    """Custom type logGmtDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixedLength = 19


_LogGmtDate_Type.__name__ = "DisplayString"
_LogGmtDate_Object = MibTableColumn
logGmtDate = _LogGmtDate_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 4),
    _LogGmtDate_Type()
)
logGmtDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logGmtDate.setStatus("mandatory")
_LogSeverity_Type = Severity
_LogSeverity_Object = MibTableColumn
logSeverity = _LogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 5),
    _LogSeverity_Type()
)
logSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSeverity.setStatus("mandatory")


class _LogMsg_Type(DisplayString):
    """Custom type logMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LogMsg_Type.__name__ = "DisplayString"
_LogMsg_Object = MibTableColumn
logMsg = _LogMsg_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 2, 1, 6),
    _LogMsg_Type()
)
logMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMsg.setStatus("mandatory")
_EventFilterTable_Object = MibTable
eventFilterTable = _EventFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3)
)
if mibBuilder.loadTexts:
    eventFilterTable.setStatus("mandatory")
_EventFilterEntry_Object = MibTableRow
eventFilterEntry = _EventFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3, 1)
)
eventFilterEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "eventFilterIndex"),
)
if mibBuilder.loadTexts:
    eventFilterEntry.setStatus("mandatory")


class _EventFilterIndex_Type(Integer32):
    """Custom type eventFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EventFilterIndex_Type.__name__ = "Integer32"
_EventFilterIndex_Object = MibTableColumn
eventFilterIndex = _EventFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3, 1, 1),
    _EventFilterIndex_Type()
)
eventFilterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventFilterIndex.setStatus("mandatory")


class _EventFilterStatus_Type(Integer32):
    """Custom type eventFilterStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("active", 2))
    )


_EventFilterStatus_Type.__name__ = "Integer32"
_EventFilterStatus_Object = MibTableColumn
eventFilterStatus = _EventFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3, 1, 2),
    _EventFilterStatus_Type()
)
eventFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventFilterStatus.setStatus("mandatory")


class _EventFilterSeverity_Type(Severity):
    """Custom type eventFilterSeverity based on Severity"""
    defaultHexValue = ""


_EventFilterSeverity_Type.__name__ = "Severity"
_EventFilterSeverity_Object = MibTableColumn
eventFilterSeverity = _EventFilterSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3, 1, 3),
    _EventFilterSeverity_Type()
)
eventFilterSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventFilterSeverity.setStatus("mandatory")


class _EventFilterSubstring_Type(DisplayString):
    """Custom type eventFilterSubstring based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_EventFilterSubstring_Type.__name__ = "DisplayString"
_EventFilterSubstring_Object = MibTableColumn
eventFilterSubstring = _EventFilterSubstring_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 3, 1, 4),
    _EventFilterSubstring_Type()
)
eventFilterSubstring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventFilterSubstring.setStatus("mandatory")
_MaintLogFilterGroup_ObjectIdentity = ObjectIdentity
maintLogFilterGroup = _MaintLogFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4)
)


class _MaintLogFilterTimeMin_Type(DisplayString):
    """Custom type maintLogFilterTimeMin based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_MaintLogFilterTimeMin_Type.__name__ = "DisplayString"
_MaintLogFilterTimeMin_Object = MibScalar
maintLogFilterTimeMin = _MaintLogFilterTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 1),
    _MaintLogFilterTimeMin_Type()
)
maintLogFilterTimeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterTimeMin.setStatus("mandatory")


class _MaintLogFilterTimeMax_Type(DisplayString):
    """Custom type maintLogFilterTimeMax based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_MaintLogFilterTimeMax_Type.__name__ = "DisplayString"
_MaintLogFilterTimeMax_Object = MibScalar
maintLogFilterTimeMax = _MaintLogFilterTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 2),
    _MaintLogFilterTimeMax_Type()
)
maintLogFilterTimeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterTimeMax.setStatus("mandatory")


class _MaintLogFilterWindow_Type(Integer32):
    """Custom type maintLogFilterWindow based on Integer32"""
    defaultValue = 30


_MaintLogFilterWindow_Type.__name__ = "Integer32"
_MaintLogFilterWindow_Object = MibScalar
maintLogFilterWindow = _MaintLogFilterWindow_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 3),
    _MaintLogFilterWindow_Type()
)
maintLogFilterWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterWindow.setStatus("mandatory")


class _MaintLogFilterNetworkNam_Type(DisplayString):
    """Custom type maintLogFilterNetworkNam based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MaintLogFilterNetworkNam_Type.__name__ = "DisplayString"
_MaintLogFilterNetworkNam_Object = MibScalar
maintLogFilterNetworkNam = _MaintLogFilterNetworkNam_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 4),
    _MaintLogFilterNetworkNam_Type()
)
maintLogFilterNetworkNam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterNetworkNam.setStatus("mandatory")


class _MaintLogFilterNodeName_Type(DisplayString):
    """Custom type maintLogFilterNodeName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MaintLogFilterNodeName_Type.__name__ = "DisplayString"
_MaintLogFilterNodeName_Object = MibScalar
maintLogFilterNodeName = _MaintLogFilterNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 5),
    _MaintLogFilterNodeName_Type()
)
maintLogFilterNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterNodeName.setStatus("mandatory")


class _MaintLogFilterSeverity_Type(Severity):
    """Custom type maintLogFilterSeverity based on Severity"""
    defaultHexValue = ""


_MaintLogFilterSeverity_Type.__name__ = "Severity"
_MaintLogFilterSeverity_Object = MibScalar
maintLogFilterSeverity = _MaintLogFilterSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 12, 4, 6),
    _MaintLogFilterSeverity_Type()
)
maintLogFilterSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLogFilterSeverity.setStatus("mandatory")
_NetworkGroup_ObjectIdentity = ObjectIdentity
networkGroup = _NetworkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 13)
)
_NetworkTable_Object = MibTable
networkTable = _NetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 13, 1)
)
if mibBuilder.loadTexts:
    networkTable.setStatus("mandatory")
_NetworkEntry_Object = MibTableRow
networkEntry = _NetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 13, 1, 1)
)
networkEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "networkName"),
)
if mibBuilder.loadTexts:
    networkEntry.setStatus("mandatory")


class _NetworkName_Type(DisplayString):
    """Custom type networkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NetworkName_Type.__name__ = "DisplayString"
_NetworkName_Object = MibTableColumn
networkName = _NetworkName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 13, 1, 1, 1),
    _NetworkName_Type()
)
networkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkName.setStatus("mandatory")
_NetworkId_Type = Integer32
_NetworkId_Object = MibTableColumn
networkId = _NetworkId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 13, 1, 1, 2),
    _NetworkId_Type()
)
networkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkId.setStatus("mandatory")
_NetworkIpxId_Type = Integer32
_NetworkIpxId_Object = MibTableColumn
networkIpxId = _NetworkIpxId_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 13, 1, 1, 3),
    _NetworkIpxId_Type()
)
networkIpxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIpxId.setStatus("mandatory")
_NodeGroup_ObjectIdentity = ObjectIdentity
nodeGroup = _NodeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 1, 14)
)
_NodeTable_Object = MibTable
nodeTable = _NodeTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 14, 1)
)
if mibBuilder.loadTexts:
    nodeTable.setStatus("mandatory")
_NodeEntry_Object = MibTableRow
nodeEntry = _NodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 14, 1, 1)
)
nodeEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "nodeNetworkName"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "nodeName"),
)
if mibBuilder.loadTexts:
    nodeEntry.setStatus("mandatory")


class _NodeNetworkName_Type(DisplayString):
    """Custom type nodeNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NodeNetworkName_Type.__name__ = "DisplayString"
_NodeNetworkName_Object = MibTableColumn
nodeNetworkName = _NodeNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 14, 1, 1, 1),
    _NodeNetworkName_Type()
)
nodeNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNetworkName.setStatus("mandatory")


class _NodeName_Type(DisplayString):
    """Custom type nodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NodeName_Type.__name__ = "DisplayString"
_NodeName_Object = MibTableColumn
nodeName = _NodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 1, 14, 1, 1, 2),
    _NodeName_Type()
)
nodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeName.setStatus("mandatory")
_Svnode_ObjectIdentity = ObjectIdentity
svnode = _Svnode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2)
)
_SvNodeGroup_ObjectIdentity = ObjectIdentity
svNodeGroup = _SvNodeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 1)
)


class _NodeGrpName_Type(DisplayString):
    """Custom type nodeGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NodeGrpName_Type.__name__ = "DisplayString"
_NodeGrpName_Object = MibScalar
nodeGrpName = _NodeGrpName_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 1),
    _NodeGrpName_Type()
)
nodeGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpName.setStatus("mandatory")


class _NodeGrpNetName_Type(DisplayString):
    """Custom type nodeGrpNetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NodeGrpNetName_Type.__name__ = "DisplayString"
_NodeGrpNetName_Object = MibScalar
nodeGrpNetName = _NodeGrpNetName_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 2),
    _NodeGrpNetName_Type()
)
nodeGrpNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpNetName.setStatus("mandatory")


class _NodeGrpAlarmState_Type(Integer32):
    """Custom type nodeGrpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("minor", 2),
          ("major", 3),
          ("unreachable", 5))
    )


_NodeGrpAlarmState_Type.__name__ = "Integer32"
_NodeGrpAlarmState_Object = MibScalar
nodeGrpAlarmState = _NodeGrpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 3),
    _NodeGrpAlarmState_Type()
)
nodeGrpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpAlarmState.setStatus("mandatory")


class _NodeGrpGateway_Type(Integer32):
    """Custom type nodeGrpGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-a-gateway", 1),
          ("gateway", 2))
    )


_NodeGrpGateway_Type.__name__ = "Integer32"
_NodeGrpGateway_Object = MibScalar
nodeGrpGateway = _NodeGrpGateway_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 4),
    _NodeGrpGateway_Type()
)
nodeGrpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpGateway.setStatus("mandatory")
_NodeGrpActive_Type = Active
_NodeGrpActive_Object = MibScalar
nodeGrpActive = _NodeGrpActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 5),
    _NodeGrpActive_Type()
)
nodeGrpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpActive.setStatus("mandatory")


class _NodeGrpPlatform_Type(Integer32):
    """Custom type nodeGrpPlatform based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipx-platform", 1),
          ("bpx-platform", 2),
          ("axis-platform", 3))
    )


_NodeGrpPlatform_Type.__name__ = "Integer32"
_NodeGrpPlatform_Object = MibScalar
nodeGrpPlatform = _NodeGrpPlatform_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 6),
    _NodeGrpPlatform_Type()
)
nodeGrpPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpPlatform.setStatus("mandatory")


class _NodeGrpRelease_Type(DisplayString):
    """Custom type nodeGrpRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NodeGrpRelease_Type.__name__ = "DisplayString"
_NodeGrpRelease_Object = MibScalar
nodeGrpRelease = _NodeGrpRelease_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 7),
    _NodeGrpRelease_Type()
)
nodeGrpRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeGrpRelease.setStatus("mandatory")
_NodeFsIncRate_Type = Integer32
_NodeFsIncRate_Object = MibScalar
nodeFsIncRate = _NodeFsIncRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 8),
    _NodeFsIncRate_Type()
)
nodeFsIncRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFsIncRate.setStatus("mandatory")
_NodeFsDecRate_Type = Integer32
_NodeFsDecRate_Object = MibScalar
nodeFsDecRate = _NodeFsDecRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 9),
    _NodeFsDecRate_Type()
)
nodeFsDecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFsDecRate.setStatus("mandatory")
_NodeFsFastRate_Type = Integer32
_NodeFsFastRate_Object = MibScalar
nodeFsFastRate = _NodeFsFastRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 10),
    _NodeFsFastRate_Type()
)
nodeFsFastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFsFastRate.setStatus("mandatory")
_NodeRstTimeout_Type = Integer32
_NodeRstTimeout_Object = MibScalar
nodeRstTimeout = _NodeRstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 11),
    _NodeRstTimeout_Type()
)
nodeRstTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRstTimeout.setStatus("mandatory")
_AlarmTrapSequenceNumber_Type = Integer32
_AlarmTrapSequenceNumber_Object = MibScalar
alarmTrapSequenceNumber = _AlarmTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 1, 12),
    _AlarmTrapSequenceNumber_Type()
)
alarmTrapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTrapSequenceNumber.setStatus("mandatory")
_PacketGroup_ObjectIdentity = ObjectIdentity
packetGroup = _PacketGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 2)
)
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("mandatory")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1)
)
trunkEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "trunkLocalSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "trunkLocalPort"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("mandatory")
_TrunkLocalSlot_Type = Integer32
_TrunkLocalSlot_Object = MibTableColumn
trunkLocalSlot = _TrunkLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 1),
    _TrunkLocalSlot_Type()
)
trunkLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkLocalSlot.setStatus("mandatory")
_TrunkLocalPort_Type = Integer32
_TrunkLocalPort_Object = MibTableColumn
trunkLocalPort = _TrunkLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 2),
    _TrunkLocalPort_Type()
)
trunkLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkLocalPort.setStatus("mandatory")
_TrunkLocalLine_Type = Integer32
_TrunkLocalLine_Object = MibTableColumn
trunkLocalLine = _TrunkLocalLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 3),
    _TrunkLocalLine_Type()
)
trunkLocalLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkLocalLine.setStatus("mandatory")


class _TrunkCardType_Type(Integer32):
    """Custom type trunkCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              22,
              31,
              34,
              103,
              104)
        )
    )
    namedValues = NamedValues(
        *(("txr", 3),
          ("bni", 4),
          ("ntc", 22),
          ("atm", 31),
          ("ait", 34),
          ("bni-t3", 103),
          ("bni-e3", 104))
    )


_TrunkCardType_Type.__name__ = "Integer32"
_TrunkCardType_Object = MibTableColumn
trunkCardType = _TrunkCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 4),
    _TrunkCardType_Type()
)
trunkCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCardType.setStatus("mandatory")


class _TrunkInterface_Type(Integer32):
    """Custom type trunkInterface based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("t1-d4", 2),
          ("t1-esf", 3),
          ("e1-30", 4),
          ("e1-31", 5),
          ("e1-32", 6),
          ("subrate", 7),
          ("atm", 8))
    )


_TrunkInterface_Type.__name__ = "Integer32"
_TrunkInterface_Object = MibTableColumn
trunkInterface = _TrunkInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 5),
    _TrunkInterface_Type()
)
trunkInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkInterface.setStatus("mandatory")
_TrunkLineLoad_Type = Integer32
_TrunkLineLoad_Object = MibTableColumn
trunkLineLoad = _TrunkLineLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 6),
    _TrunkLineLoad_Type()
)
trunkLineLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkLineLoad.setStatus("mandatory")
_TrunkRemNodeId_Type = Integer32
_TrunkRemNodeId_Object = MibTableColumn
trunkRemNodeId = _TrunkRemNodeId_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 7),
    _TrunkRemNodeId_Type()
)
trunkRemNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRemNodeId.setStatus("mandatory")
_TrunkRemLineNumber_Type = Integer32
_TrunkRemLineNumber_Object = MibTableColumn
trunkRemLineNumber = _TrunkRemLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 8),
    _TrunkRemLineNumber_Type()
)
trunkRemLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRemLineNumber.setStatus("mandatory")
_TrunkRemSlot_Type = Integer32
_TrunkRemSlot_Object = MibTableColumn
trunkRemSlot = _TrunkRemSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 9),
    _TrunkRemSlot_Type()
)
trunkRemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRemSlot.setStatus("mandatory")
_TrunkRemPort_Type = Integer32
_TrunkRemPort_Object = MibTableColumn
trunkRemPort = _TrunkRemPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 10),
    _TrunkRemPort_Type()
)
trunkRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRemPort.setStatus("mandatory")


class _TrunkAlarmState_Type(Integer32):
    """Custom type trunkAlarmState based on Integer32"""
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
        *(("clear", 1),
          ("info", 2),
          ("minor", 3),
          ("major", 4))
    )


_TrunkAlarmState_Type.__name__ = "Integer32"
_TrunkAlarmState_Object = MibTableColumn
trunkAlarmState = _TrunkAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 11),
    _TrunkAlarmState_Type()
)
trunkAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkAlarmState.setStatus("mandatory")


class _TrunkComment_Type(DisplayString):
    """Custom type trunkComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TrunkComment_Type.__name__ = "DisplayString"
_TrunkComment_Object = MibTableColumn
trunkComment = _TrunkComment_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 12),
    _TrunkComment_Type()
)
trunkComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkComment.setStatus("mandatory")
_TrunkActive_Type = Active
_TrunkActive_Object = MibTableColumn
trunkActive = _TrunkActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 13),
    _TrunkActive_Type()
)
trunkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkActive.setStatus("mandatory")


class _TrunkStatus_Type(Integer32):
    """Custom type trunkStatus based on Integer32"""
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
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4))
    )


_TrunkStatus_Type.__name__ = "Integer32"
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 14),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("mandatory")
_TrunkStatReserve_Type = Integer32
_TrunkStatReserve_Object = MibTableColumn
trunkStatReserve = _TrunkStatReserve_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 15),
    _TrunkStatReserve_Type()
)
trunkStatReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkStatReserve.setStatus("mandatory")
_TrunkBurstyDataBQDepth_Type = Integer32
_TrunkBurstyDataBQDepth_Object = MibTableColumn
trunkBurstyDataBQDepth = _TrunkBurstyDataBQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 16),
    _TrunkBurstyDataBQDepth_Type()
)
trunkBurstyDataBQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkBurstyDataBQDepth.setStatus("mandatory")
_TrunkBurstyDataBQEfcnThreshold_Type = Integer32
_TrunkBurstyDataBQEfcnThreshold_Object = MibTableColumn
trunkBurstyDataBQEfcnThreshold = _TrunkBurstyDataBQEfcnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 17),
    _TrunkBurstyDataBQEfcnThreshold_Type()
)
trunkBurstyDataBQEfcnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkBurstyDataBQEfcnThreshold.setStatus("mandatory")
_TrunkClpHighDropThreshold_Type = Integer32
_TrunkClpHighDropThreshold_Object = MibTableColumn
trunkClpHighDropThreshold = _TrunkClpHighDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 18),
    _TrunkClpHighDropThreshold_Type()
)
trunkClpHighDropThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkClpHighDropThreshold.setStatus("mandatory")
_TrunkClpLowDropThreshold_Type = Integer32
_TrunkClpLowDropThreshold_Object = MibTableColumn
trunkClpLowDropThreshold = _TrunkClpLowDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 2, 2, 1, 19),
    _TrunkClpLowDropThreshold_Type()
)
trunkClpLowDropThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkClpLowDropThreshold.setStatus("mandatory")
_CircuitGroup_ObjectIdentity = ObjectIdentity
circuitGroup = _CircuitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 3)
)
_CirLineTable_Object = MibTable
cirLineTable = _CirLineTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cirLineTable.setStatus("mandatory")
_CirLineEntry_Object = MibTableRow
cirLineEntry = _CirLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1)
)
cirLineEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "cirLineLineNumber"),
)
if mibBuilder.loadTexts:
    cirLineEntry.setStatus("mandatory")
_CirLineLineNumber_Type = Integer32
_CirLineLineNumber_Object = MibTableColumn
cirLineLineNumber = _CirLineLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 3),
    _CirLineLineNumber_Type()
)
cirLineLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineLineNumber.setStatus("mandatory")


class _CirLineCardType_Type(Integer32):
    """Custom type cirLineCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              21,
              29)
        )
    )
    namedValues = NamedValues(
        *(("txr", 3),
          ("cip", 21),
          ("cdp", 29))
    )


_CirLineCardType_Type.__name__ = "Integer32"
_CirLineCardType_Object = MibTableColumn
cirLineCardType = _CirLineCardType_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 4),
    _CirLineCardType_Type()
)
cirLineCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineCardType.setStatus("mandatory")


class _CirLineInterface_Type(Integer32):
    """Custom type cirLineInterface based on Integer32"""
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
          ("t1", 2),
          ("e1", 3))
    )


_CirLineInterface_Type.__name__ = "Integer32"
_CirLineInterface_Object = MibTableColumn
cirLineInterface = _CirLineInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 5),
    _CirLineInterface_Type()
)
cirLineInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineInterface.setStatus("mandatory")


class _CirLineComment_Type(DisplayString):
    """Custom type cirLineComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_CirLineComment_Type.__name__ = "DisplayString"
_CirLineComment_Object = MibTableColumn
cirLineComment = _CirLineComment_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 6),
    _CirLineComment_Type()
)
cirLineComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineComment.setStatus("mandatory")
_CirLineActive_Type = Active
_CirLineActive_Object = MibTableColumn
cirLineActive = _CirLineActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 7),
    _CirLineActive_Type()
)
cirLineActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineActive.setStatus("mandatory")


class _CirLineStatus_Type(Integer32):
    """Custom type cirLineStatus based on Integer32"""
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
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4))
    )


_CirLineStatus_Type.__name__ = "Integer32"
_CirLineStatus_Object = MibTableColumn
cirLineStatus = _CirLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 3, 1, 1, 8),
    _CirLineStatus_Type()
)
cirLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineStatus.setStatus("mandatory")
_FrpGroup_ObjectIdentity = ObjectIdentity
frpGroup = _FrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 4)
)
_FrpTable_Object = MibTable
frpTable = _FrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1)
)
if mibBuilder.loadTexts:
    frpTable.setStatus("obsolete")
_FrpEntry_Object = MibTableRow
frpEntry = _FrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1)
)
frpEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "frpLocalSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "frpLocalPort"),
)
if mibBuilder.loadTexts:
    frpEntry.setStatus("obsolete")
_FrpLocalSlot_Type = Integer32
_FrpLocalSlot_Object = MibTableColumn
frpLocalSlot = _FrpLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 3),
    _FrpLocalSlot_Type()
)
frpLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpLocalSlot.setStatus("obsolete")
_FrpLocalPort_Type = Integer32
_FrpLocalPort_Object = MibTableColumn
frpLocalPort = _FrpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 4),
    _FrpLocalPort_Type()
)
frpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpLocalPort.setStatus("obsolete")
_FrpPortSpeed_Type = Integer32
_FrpPortSpeed_Object = MibTableColumn
frpPortSpeed = _FrpPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 5),
    _FrpPortSpeed_Type()
)
frpPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpPortSpeed.setStatus("obsolete")


class _FrpComment_Type(DisplayString):
    """Custom type frpComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_FrpComment_Type.__name__ = "DisplayString"
_FrpComment_Object = MibTableColumn
frpComment = _FrpComment_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 6),
    _FrpComment_Type()
)
frpComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpComment.setStatus("obsolete")
_FrpActive_Type = Active
_FrpActive_Object = MibTableColumn
frpActive = _FrpActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 7),
    _FrpActive_Type()
)
frpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpActive.setStatus("obsolete")


class _FrpStatus_Type(Integer32):
    """Custom type frpStatus based on Integer32"""
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
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4))
    )


_FrpStatus_Type.__name__ = "Integer32"
_FrpStatus_Object = MibTableColumn
frpStatus = _FrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 8),
    _FrpStatus_Type()
)
frpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpStatus.setStatus("obsolete")
_FrpQDepth_Type = Integer32
_FrpQDepth_Object = MibTableColumn
frpQDepth = _FrpQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 9),
    _FrpQDepth_Type()
)
frpQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpQDepth.setStatus("obsolete")
_FrpEcnThreshold_Type = Integer32
_FrpEcnThreshold_Object = MibTableColumn
frpEcnThreshold = _FrpEcnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 10),
    _FrpEcnThreshold_Type()
)
frpEcnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpEcnThreshold.setStatus("obsolete")
_FrpDeThreshold_Type = Integer32
_FrpDeThreshold_Object = MibTableColumn
frpDeThreshold = _FrpDeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 11),
    _FrpDeThreshold_Type()
)
frpDeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpDeThreshold.setStatus("obsolete")


class _FrpPortType_Type(Integer32):
    """Custom type frpPortType based on Integer32"""
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
        *(("uni", 1),
          ("nni", 2),
          ("aip", 3),
          ("not-defined", 4),
          ("frsm", 5),
          ("portConcent", 6))
    )


_FrpPortType_Type.__name__ = "Integer32"
_FrpPortType_Object = MibTableColumn
frpPortType = _FrpPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 12),
    _FrpPortType_Type()
)
frpPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpPortType.setStatus("obsolete")
_FrpLocalLine_Type = Integer32
_FrpLocalLine_Object = MibTableColumn
frpLocalLine = _FrpLocalLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 4, 1, 1, 13),
    _FrpLocalLine_Type()
)
frpLocalLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpLocalLine.setStatus("mandatory")
_ConnGroup_ObjectIdentity = ObjectIdentity
connGroup = _ConnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 5)
)
_ConnTable_Object = MibTable
connTable = _ConnTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1)
)
if mibBuilder.loadTexts:
    connTable.setStatus("obsolete")
_ConnEntry_Object = MibTableRow
connEntry = _ConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1)
)
connEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "connLocalSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "connLocalChannel"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "connLocalDLCI"),
)
if mibBuilder.loadTexts:
    connEntry.setStatus("mandatory")
_ConnLocalSlot_Type = Integer32
_ConnLocalSlot_Object = MibTableColumn
connLocalSlot = _ConnLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 3),
    _ConnLocalSlot_Type()
)
connLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalSlot.setStatus("mandatory")
_ConnLocalChannel_Type = Integer32
_ConnLocalChannel_Object = MibTableColumn
connLocalChannel = _ConnLocalChannel_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 4),
    _ConnLocalChannel_Type()
)
connLocalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalChannel.setStatus("mandatory")
_ConnLocalDLCI_Type = Integer32
_ConnLocalDLCI_Object = MibTableColumn
connLocalDLCI = _ConnLocalDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 5),
    _ConnLocalDLCI_Type()
)
connLocalDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalDLCI.setStatus("mandatory")
_ConnRemoteNodeId_Type = Integer32
_ConnRemoteNodeId_Object = MibTableColumn
connRemoteNodeId = _ConnRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 6),
    _ConnRemoteNodeId_Type()
)
connRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteNodeId.setStatus("mandatory")
_ConnRemoteSlot_Type = Integer32
_ConnRemoteSlot_Object = MibTableColumn
connRemoteSlot = _ConnRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 7),
    _ConnRemoteSlot_Type()
)
connRemoteSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteSlot.setStatus("mandatory")
_ConnRemoteChannel_Type = Integer32
_ConnRemoteChannel_Object = MibTableColumn
connRemoteChannel = _ConnRemoteChannel_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 8),
    _ConnRemoteChannel_Type()
)
connRemoteChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteChannel.setStatus("mandatory")
_ConnRemoteDLCI_Type = Integer32
_ConnRemoteDLCI_Object = MibTableColumn
connRemoteDLCI = _ConnRemoteDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 9),
    _ConnRemoteDLCI_Type()
)
connRemoteDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteDLCI.setStatus("mandatory")


class _ConnType_Type(Integer32):
    """Custom type connType based on Integer32"""
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
        *(("voice-dsi-adpcm", 1),
          ("voice-dsi", 2),
          ("voice", 3),
          ("voice-adpcm", 4),
          ("data", 5),
          ("frame-relay", 6))
    )


_ConnType_Type.__name__ = "Integer32"
_ConnType_Object = MibTableColumn
connType = _ConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 10),
    _ConnType_Type()
)
connType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connType.setStatus("mandatory")
_ConnRate_Type = Integer32
_ConnRate_Object = MibTableColumn
connRate = _ConnRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 11),
    _ConnRate_Type()
)
connRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRate.setStatus("mandatory")
_ConnLocalMaxPkts_Type = Integer32
_ConnLocalMaxPkts_Object = MibTableColumn
connLocalMaxPkts = _ConnLocalMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 12),
    _ConnLocalMaxPkts_Type()
)
connLocalMaxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalMaxPkts.setStatus("mandatory")
_ConnRemoteMaxPkts_Type = Integer32
_ConnRemoteMaxPkts_Object = MibTableColumn
connRemoteMaxPkts = _ConnRemoteMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 13),
    _ConnRemoteMaxPkts_Type()
)
connRemoteMaxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRemoteMaxPkts.setStatus("mandatory")
_ConnMinBandwidth_Type = Integer32
_ConnMinBandwidth_Object = MibTableColumn
connMinBandwidth = _ConnMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 14),
    _ConnMinBandwidth_Type()
)
connMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMinBandwidth.setStatus("mandatory")


class _ConnDAX_Type(Integer32):
    """Custom type connDAX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-dax", 1),
          ("dax", 2))
    )


_ConnDAX_Type.__name__ = "Integer32"
_ConnDAX_Object = MibTableColumn
connDAX = _ConnDAX_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 15),
    _ConnDAX_Type()
)
connDAX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connDAX.setStatus("mandatory")


class _ConnTXR_Type(Integer32):
    """Custom type connTXR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-txr", 1),
          ("txr", 2))
    )


_ConnTXR_Type.__name__ = "Integer32"
_ConnTXR_Object = MibTableColumn
connTXR = _ConnTXR_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 16),
    _ConnTXR_Type()
)
connTXR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connTXR.setStatus("mandatory")


class _ConnComment_Type(DisplayString):
    """Custom type connComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_ConnComment_Type.__name__ = "DisplayString"
_ConnComment_Object = MibTableColumn
connComment = _ConnComment_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 17),
    _ConnComment_Type()
)
connComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connComment.setStatus("mandatory")
_ConnActive_Type = Active
_ConnActive_Object = MibTableColumn
connActive = _ConnActive_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 18),
    _ConnActive_Type()
)
connActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connActive.setStatus("mandatory")


class _ConnStatus_Type(Integer32):
    """Custom type connStatus based on Integer32"""
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
        *(("inactive", 1),
          ("clear", 2),
          ("fail", 3),
          ("down", 4))
    )


_ConnStatus_Type.__name__ = "Integer32"
_ConnStatus_Object = MibTableColumn
connStatus = _ConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 19),
    _ConnStatus_Type()
)
connStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connStatus.setStatus("mandatory")
_ConnQir_Type = Integer32
_ConnQir_Object = MibTableColumn
connQir = _ConnQir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 20),
    _ConnQir_Type()
)
connQir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connQir.setStatus("mandatory")
_ConnPir_Type = Integer32
_ConnPir_Object = MibTableColumn
connPir = _ConnPir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 21),
    _ConnPir_Type()
)
connPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPir.setStatus("mandatory")
_ConnVcQueDepth_Type = Integer32
_ConnVcQueDepth_Object = MibTableColumn
connVcQueDepth = _ConnVcQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 22),
    _ConnVcQueDepth_Type()
)
connVcQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connVcQueDepth.setStatus("mandatory")
_ConnVcQueThreshold_Type = Integer32
_ConnVcQueThreshold_Object = MibTableColumn
connVcQueThreshold = _ConnVcQueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 23),
    _ConnVcQueThreshold_Type()
)
connVcQueThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connVcQueThreshold.setStatus("mandatory")
_ConnCMax_Type = Integer32
_ConnCMax_Object = MibTableColumn
connCMax = _ConnCMax_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 24),
    _ConnCMax_Type()
)
connCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCMax.setStatus("mandatory")
_ConnPerUtil_Type = Integer32
_ConnPerUtil_Object = MibTableColumn
connPerUtil = _ConnPerUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 25),
    _ConnPerUtil_Type()
)
connPerUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPerUtil.setStatus("mandatory")
_ConnConnInfoFlag_Type = Integer32
_ConnConnInfoFlag_Object = MibTableColumn
connConnInfoFlag = _ConnConnInfoFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 26),
    _ConnConnInfoFlag_Type()
)
connConnInfoFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConnInfoFlag.setStatus("mandatory")
_ConnCir_Type = Integer32
_ConnCir_Object = MibTableColumn
connCir = _ConnCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 27),
    _ConnCir_Type()
)
connCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCir.setStatus("mandatory")
_ConnABitStatus_Type = Integer32
_ConnABitStatus_Object = MibTableColumn
connABitStatus = _ConnABitStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 28),
    _ConnABitStatus_Type()
)
connABitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connABitStatus.setStatus("mandatory")
_ConnLocalLine_Type = Integer32
_ConnLocalLine_Object = MibTableColumn
connLocalLine = _ConnLocalLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 5, 1, 1, 29),
    _ConnLocalLine_Type()
)
connLocalLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLocalLine.setStatus("mandatory")
_RealTimeCountersGroup_ObjectIdentity = ObjectIdentity
realTimeCountersGroup = _RealTimeCountersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 2, 6)
)
_CirLineRTCTable_Object = MibTable
cirLineRTCTable = _CirLineRTCTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2)
)
if mibBuilder.loadTexts:
    cirLineRTCTable.setStatus("mandatory")
_CirLineRTCEntry_Object = MibTableRow
cirLineRTCEntry = _CirLineRTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1)
)
cirLineRTCEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "cirLineRTCLineNumber"),
)
if mibBuilder.loadTexts:
    cirLineRTCEntry.setStatus("mandatory")
_CirLineRTCLineNumber_Type = Integer32
_CirLineRTCLineNumber_Object = MibTableColumn
cirLineRTCLineNumber = _CirLineRTCLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 1),
    _CirLineRTCLineNumber_Type()
)
cirLineRTCLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCLineNumber.setStatus("mandatory")
_CirLineRTCBipolarViolations_Type = Counter32
_CirLineRTCBipolarViolations_Object = MibTableColumn
cirLineRTCBipolarViolations = _CirLineRTCBipolarViolations_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 4),
    _CirLineRTCBipolarViolations_Type()
)
cirLineRTCBipolarViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCBipolarViolations.setStatus("mandatory")
_CirLineRTCFrameSlips_Type = Counter32
_CirLineRTCFrameSlips_Object = MibTableColumn
cirLineRTCFrameSlips = _CirLineRTCFrameSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 5),
    _CirLineRTCFrameSlips_Type()
)
cirLineRTCFrameSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCFrameSlips.setStatus("mandatory")
_CirLineRTCOutOfFrames_Type = Counter32
_CirLineRTCOutOfFrames_Object = MibTableColumn
cirLineRTCOutOfFrames = _CirLineRTCOutOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 6),
    _CirLineRTCOutOfFrames_Type()
)
cirLineRTCOutOfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCOutOfFrames.setStatus("mandatory")
_CirLineRTCLossesOfSignal_Type = Counter32
_CirLineRTCLossesOfSignal_Object = MibTableColumn
cirLineRTCLossesOfSignal = _CirLineRTCLossesOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 7),
    _CirLineRTCLossesOfSignal_Type()
)
cirLineRTCLossesOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCLossesOfSignal.setStatus("mandatory")
_CirLineRTCFrameBitErrors_Type = Counter32
_CirLineRTCFrameBitErrors_Object = MibTableColumn
cirLineRTCFrameBitErrors = _CirLineRTCFrameBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 8),
    _CirLineRTCFrameBitErrors_Type()
)
cirLineRTCFrameBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCFrameBitErrors.setStatus("mandatory")
_CirLineRTCCrcErrors_Type = Counter32
_CirLineRTCCrcErrors_Object = MibTableColumn
cirLineRTCCrcErrors = _CirLineRTCCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 9),
    _CirLineRTCCrcErrors_Type()
)
cirLineRTCCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCCrcErrors.setStatus("mandatory")
_CirLineRTCOutOfMultiFrames_Type = Counter32
_CirLineRTCOutOfMultiFrames_Object = MibTableColumn
cirLineRTCOutOfMultiFrames = _CirLineRTCOutOfMultiFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 10),
    _CirLineRTCOutOfMultiFrames_Type()
)
cirLineRTCOutOfMultiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCOutOfMultiFrames.setStatus("mandatory")
_CirLineRTCAllOnesInTimeslot16_Type = Counter32
_CirLineRTCAllOnesInTimeslot16_Object = MibTableColumn
cirLineRTCAllOnesInTimeslot16 = _CirLineRTCAllOnesInTimeslot16_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 2, 1, 11),
    _CirLineRTCAllOnesInTimeslot16_Type()
)
cirLineRTCAllOnesInTimeslot16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cirLineRTCAllOnesInTimeslot16.setStatus("mandatory")
_FrpRTCTable_Object = MibTable
frpRTCTable = _FrpRTCTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3)
)
if mibBuilder.loadTexts:
    frpRTCTable.setStatus("mandatory")
_FrpRTCEntry_Object = MibTableRow
frpRTCEntry = _FrpRTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1)
)
frpRTCEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "frpRTCSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "frpRTCPort"),
)
if mibBuilder.loadTexts:
    frpRTCEntry.setStatus("mandatory")
_FrpRTCSlot_Type = Integer32
_FrpRTCSlot_Object = MibTableColumn
frpRTCSlot = _FrpRTCSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 1),
    _FrpRTCSlot_Type()
)
frpRTCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCSlot.setStatus("mandatory")
_FrpRTCPort_Type = Integer32
_FrpRTCPort_Object = MibTableColumn
frpRTCPort = _FrpRTCPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 2),
    _FrpRTCPort_Type()
)
frpRTCPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCPort.setStatus("mandatory")
_FrpRTCFramesRcvd_Type = Counter32
_FrpRTCFramesRcvd_Object = MibTableColumn
frpRTCFramesRcvd = _FrpRTCFramesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 4),
    _FrpRTCFramesRcvd_Type()
)
frpRTCFramesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvd.setStatus("mandatory")
_FrpRTCFramesXmitted_Type = Counter32
_FrpRTCFramesXmitted_Object = MibTableColumn
frpRTCFramesXmitted = _FrpRTCFramesXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 5),
    _FrpRTCFramesXmitted_Type()
)
frpRTCFramesXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesXmitted.setStatus("mandatory")
_FrpRTCBytesRcvd_Type = Counter32
_FrpRTCBytesRcvd_Object = MibTableColumn
frpRTCBytesRcvd = _FrpRTCBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 6),
    _FrpRTCBytesRcvd_Type()
)
frpRTCBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCBytesRcvd.setStatus("mandatory")
_FrpRTCBytesXmitted_Type = Counter32
_FrpRTCBytesXmitted_Object = MibTableColumn
frpRTCBytesXmitted = _FrpRTCBytesXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 7),
    _FrpRTCBytesXmitted_Type()
)
frpRTCBytesXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCBytesXmitted.setStatus("mandatory")
_FrpRTCFramesXmittedWithFECN_Type = Counter32
_FrpRTCFramesXmittedWithFECN_Object = MibTableColumn
frpRTCFramesXmittedWithFECN = _FrpRTCFramesXmittedWithFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 8),
    _FrpRTCFramesXmittedWithFECN_Type()
)
frpRTCFramesXmittedWithFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesXmittedWithFECN.setStatus("mandatory")
_FrpRTCFramesXmittedWithBECN_Type = Counter32
_FrpRTCFramesXmittedWithBECN_Object = MibTableColumn
frpRTCFramesXmittedWithBECN = _FrpRTCFramesXmittedWithBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 9),
    _FrpRTCFramesXmittedWithBECN_Type()
)
frpRTCFramesXmittedWithBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesXmittedWithBECN.setStatus("mandatory")
_FrpRTCFramesRcvdCrcErrors_Type = Counter32
_FrpRTCFramesRcvdCrcErrors_Object = MibTableColumn
frpRTCFramesRcvdCrcErrors = _FrpRTCFramesRcvdCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 10),
    _FrpRTCFramesRcvdCrcErrors_Type()
)
frpRTCFramesRcvdCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvdCrcErrors.setStatus("mandatory")
_FrpRTCFramesRcvdInvalidFormat_Type = Counter32
_FrpRTCFramesRcvdInvalidFormat_Object = MibTableColumn
frpRTCFramesRcvdInvalidFormat = _FrpRTCFramesRcvdInvalidFormat_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 11),
    _FrpRTCFramesRcvdInvalidFormat_Type()
)
frpRTCFramesRcvdInvalidFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvdInvalidFormat.setStatus("mandatory")
_FrpRTCFramesRcvdAlignmentErrors_Type = Counter32
_FrpRTCFramesRcvdAlignmentErrors_Object = MibTableColumn
frpRTCFramesRcvdAlignmentErrors = _FrpRTCFramesRcvdAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 12),
    _FrpRTCFramesRcvdAlignmentErrors_Type()
)
frpRTCFramesRcvdAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvdAlignmentErrors.setStatus("mandatory")
_FrpRTCFramesRcvdIllegalLen_Type = Counter32
_FrpRTCFramesRcvdIllegalLen_Object = MibTableColumn
frpRTCFramesRcvdIllegalLen = _FrpRTCFramesRcvdIllegalLen_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 13),
    _FrpRTCFramesRcvdIllegalLen_Type()
)
frpRTCFramesRcvdIllegalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvdIllegalLen.setStatus("mandatory")
_FrpRTCDmaOverruns_Type = Counter32
_FrpRTCDmaOverruns_Object = MibTableColumn
frpRTCDmaOverruns = _FrpRTCDmaOverruns_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 14),
    _FrpRTCDmaOverruns_Type()
)
frpRTCDmaOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCDmaOverruns.setStatus("mandatory")
_FrpRTCLmiStatusEnquires_Type = Counter32
_FrpRTCLmiStatusEnquires_Object = MibTableColumn
frpRTCLmiStatusEnquires = _FrpRTCLmiStatusEnquires_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 15),
    _FrpRTCLmiStatusEnquires_Type()
)
frpRTCLmiStatusEnquires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiStatusEnquires.setStatus("mandatory")
_FrpRTCLmiStatusXmitRate_Type = Counter32
_FrpRTCLmiStatusXmitRate_Object = MibTableColumn
frpRTCLmiStatusXmitRate = _FrpRTCLmiStatusXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 16),
    _FrpRTCLmiStatusXmitRate_Type()
)
frpRTCLmiStatusXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiStatusXmitRate.setStatus("mandatory")
_FrpRTCLmiStatusUpdateRate_Type = Counter32
_FrpRTCLmiStatusUpdateRate_Object = MibTableColumn
frpRTCLmiStatusUpdateRate = _FrpRTCLmiStatusUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 17),
    _FrpRTCLmiStatusUpdateRate_Type()
)
frpRTCLmiStatusUpdateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiStatusUpdateRate.setStatus("mandatory")
_FrpRTCLmiInvalidStatusEnquires_Type = Counter32
_FrpRTCLmiInvalidStatusEnquires_Object = MibTableColumn
frpRTCLmiInvalidStatusEnquires = _FrpRTCLmiInvalidStatusEnquires_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 18),
    _FrpRTCLmiInvalidStatusEnquires_Type()
)
frpRTCLmiInvalidStatusEnquires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiInvalidStatusEnquires.setStatus("mandatory")
_FrpRTCLmiLinkTimeoutErrors_Type = Counter32
_FrpRTCLmiLinkTimeoutErrors_Object = MibTableColumn
frpRTCLmiLinkTimeoutErrors = _FrpRTCLmiLinkTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 19),
    _FrpRTCLmiLinkTimeoutErrors_Type()
)
frpRTCLmiLinkTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiLinkTimeoutErrors.setStatus("mandatory")
_FrpRTCLmiKeepaliveSequenceErrors_Type = Counter32
_FrpRTCLmiKeepaliveSequenceErrors_Object = MibTableColumn
frpRTCLmiKeepaliveSequenceErrors = _FrpRTCLmiKeepaliveSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 20),
    _FrpRTCLmiKeepaliveSequenceErrors_Type()
)
frpRTCLmiKeepaliveSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLmiKeepaliveSequenceErrors.setStatus("mandatory")
_FrpRTCFramesRcvdUndefDlciErrors_Type = Counter32
_FrpRTCFramesRcvdUndefDlciErrors_Object = MibTableColumn
frpRTCFramesRcvdUndefDlciErrors = _FrpRTCFramesRcvdUndefDlciErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 21),
    _FrpRTCFramesRcvdUndefDlciErrors_Type()
)
frpRTCFramesRcvdUndefDlciErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCFramesRcvdUndefDlciErrors.setStatus("mandatory")
_FrpRTCXmitStatusEnquirey_Type = Counter32
_FrpRTCXmitStatusEnquirey_Object = MibTableColumn
frpRTCXmitStatusEnquirey = _FrpRTCXmitStatusEnquirey_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 22),
    _FrpRTCXmitStatusEnquirey_Type()
)
frpRTCXmitStatusEnquirey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCXmitStatusEnquirey.setStatus("mandatory")
_FrpRTCRxStatusCounter_Type = Counter32
_FrpRTCRxStatusCounter_Object = MibTableColumn
frpRTCRxStatusCounter = _FrpRTCRxStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 23),
    _FrpRTCRxStatusCounter_Type()
)
frpRTCRxStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCRxStatusCounter.setStatus("mandatory")
_FrpRTCAsyncStatusCounter_Type = Counter32
_FrpRTCAsyncStatusCounter_Object = MibTableColumn
frpRTCAsyncStatusCounter = _FrpRTCAsyncStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 24),
    _FrpRTCAsyncStatusCounter_Type()
)
frpRTCAsyncStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCAsyncStatusCounter.setStatus("mandatory")
_FrpRTCBadSequenceNumberCount_Type = Counter32
_FrpRTCBadSequenceNumberCount_Object = MibTableColumn
frpRTCBadSequenceNumberCount = _FrpRTCBadSequenceNumberCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 25),
    _FrpRTCBadSequenceNumberCount_Type()
)
frpRTCBadSequenceNumberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCBadSequenceNumberCount.setStatus("mandatory")
_FrpRTCTxProtocolTimeOutCount_Type = Counter32
_FrpRTCTxProtocolTimeOutCount_Object = MibTableColumn
frpRTCTxProtocolTimeOutCount = _FrpRTCTxProtocolTimeOutCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 26),
    _FrpRTCTxProtocolTimeOutCount_Type()
)
frpRTCTxProtocolTimeOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCTxProtocolTimeOutCount.setStatus("mandatory")
_FrpRTCCLLMFramesTx_Type = Counter32
_FrpRTCCLLMFramesTx_Object = MibTableColumn
frpRTCCLLMFramesTx = _FrpRTCCLLMFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 27),
    _FrpRTCCLLMFramesTx_Type()
)
frpRTCCLLMFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCCLLMFramesTx.setStatus("mandatory")
_FrpRTCCLLMBytesTx_Type = Counter32
_FrpRTCCLLMBytesTx_Object = MibTableColumn
frpRTCCLLMBytesTx = _FrpRTCCLLMBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 28),
    _FrpRTCCLLMBytesTx_Type()
)
frpRTCCLLMBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCCLLMBytesTx.setStatus("mandatory")
_FrpRTCCLLMFramesRx_Type = Counter32
_FrpRTCCLLMFramesRx_Object = MibTableColumn
frpRTCCLLMFramesRx = _FrpRTCCLLMFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 29),
    _FrpRTCCLLMFramesRx_Type()
)
frpRTCCLLMFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCCLLMFramesRx.setStatus("mandatory")
_FrpRTCCLLMBytes_Type = Counter32
_FrpRTCCLLMBytes_Object = MibScalar
frpRTCCLLMBytes = _FrpRTCCLLMBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 30),
    _FrpRTCCLLMBytes_Type()
)
frpRTCCLLMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCCLLMBytes.setStatus("mandatory")
_FrpRTCCLLMFailures_Type = Counter32
_FrpRTCCLLMFailures_Object = MibTableColumn
frpRTCCLLMFailures = _FrpRTCCLLMFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 31),
    _FrpRTCCLLMFailures_Type()
)
frpRTCCLLMFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCCLLMFailures.setStatus("mandatory")
_FrpRTCRxDEFramesDiscarded_Type = Counter32
_FrpRTCRxDEFramesDiscarded_Object = MibTableColumn
frpRTCRxDEFramesDiscarded = _FrpRTCRxDEFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 32),
    _FrpRTCRxDEFramesDiscarded_Type()
)
frpRTCRxDEFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCRxDEFramesDiscarded.setStatus("mandatory")
_FrpRTCLine_Type = Integer32
_FrpRTCLine_Object = MibTableColumn
frpRTCLine = _FrpRTCLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 3, 1, 33),
    _FrpRTCLine_Type()
)
frpRTCLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpRTCLine.setStatus("mandatory")
_ConnRTCTable_Object = MibTable
connRTCTable = _ConnRTCTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4)
)
if mibBuilder.loadTexts:
    connRTCTable.setStatus("mandatory")
_ConnRTCEntry_Object = MibTableRow
connRTCEntry = _ConnRTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1)
)
connRTCEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "connRTCSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "connRTCChannel"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "connRTCDLCI"),
)
if mibBuilder.loadTexts:
    connRTCEntry.setStatus("mandatory")
_ConnRTCSlot_Type = Integer32
_ConnRTCSlot_Object = MibTableColumn
connRTCSlot = _ConnRTCSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 1),
    _ConnRTCSlot_Type()
)
connRTCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCSlot.setStatus("mandatory")
_ConnRTCChannel_Type = Integer32
_ConnRTCChannel_Object = MibTableColumn
connRTCChannel = _ConnRTCChannel_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 2),
    _ConnRTCChannel_Type()
)
connRTCChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCChannel.setStatus("mandatory")
_ConnRTCDLCI_Type = Integer32
_ConnRTCDLCI_Object = MibTableColumn
connRTCDLCI = _ConnRTCDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 3),
    _ConnRTCDLCI_Type()
)
connRTCDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCDLCI.setStatus("mandatory")
_ConnRTCRcvdFrames_Type = Counter32
_ConnRTCRcvdFrames_Object = MibTableColumn
connRTCRcvdFrames = _ConnRTCRcvdFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 4),
    _ConnRTCRcvdFrames_Type()
)
connRTCRcvdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdFrames.setStatus("mandatory")
_ConnRTCRcvdFramesDiscarded_Type = Counter32
_ConnRTCRcvdFramesDiscarded_Object = MibTableColumn
connRTCRcvdFramesDiscarded = _ConnRTCRcvdFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 5),
    _ConnRTCRcvdFramesDiscarded_Type()
)
connRTCRcvdFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdFramesDiscarded.setStatus("mandatory")
_ConnRTCXmitFrames_Type = Counter32
_ConnRTCXmitFrames_Object = MibTableColumn
connRTCXmitFrames = _ConnRTCXmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 6),
    _ConnRTCXmitFrames_Type()
)
connRTCXmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitFrames.setStatus("mandatory")
_ConnRTCXmitFramesDiscarded_Type = Counter32
_ConnRTCXmitFramesDiscarded_Object = MibTableColumn
connRTCXmitFramesDiscarded = _ConnRTCXmitFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 7),
    _ConnRTCXmitFramesDiscarded_Type()
)
connRTCXmitFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitFramesDiscarded.setStatus("mandatory")
_ConnRTCRcvdPkts_Type = Counter32
_ConnRTCRcvdPkts_Object = MibTableColumn
connRTCRcvdPkts = _ConnRTCRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 8),
    _ConnRTCRcvdPkts_Type()
)
connRTCRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdPkts.setStatus("mandatory")
_ConnRTCRcvdPktsDiscarded_Type = Counter32
_ConnRTCRcvdPktsDiscarded_Object = MibTableColumn
connRTCRcvdPktsDiscarded = _ConnRTCRcvdPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 9),
    _ConnRTCRcvdPktsDiscarded_Type()
)
connRTCRcvdPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdPktsDiscarded.setStatus("mandatory")
_ConnRTCXmitPkts_Type = Counter32
_ConnRTCXmitPkts_Object = MibTableColumn
connRTCXmitPkts = _ConnRTCXmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 10),
    _ConnRTCXmitPkts_Type()
)
connRTCXmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitPkts.setStatus("mandatory")
_ConnRTCXmitPktsProjected_Type = Counter32
_ConnRTCXmitPktsProjected_Object = MibTableColumn
connRTCXmitPktsProjected = _ConnRTCXmitPktsProjected_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 11),
    _ConnRTCXmitPktsProjected_Type()
)
connRTCXmitPktsProjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitPktsProjected.setStatus("mandatory")
_ConnRTCXmitPktsSupervisory_Type = Counter32
_ConnRTCXmitPktsSupervisory_Object = MibTableColumn
connRTCXmitPktsSupervisory = _ConnRTCXmitPktsSupervisory_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 12),
    _ConnRTCXmitPktsSupervisory_Type()
)
connRTCXmitPktsSupervisory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitPktsSupervisory.setStatus("mandatory")
_ConnRTCRcvdBytes_Type = Counter32
_ConnRTCRcvdBytes_Object = MibTableColumn
connRTCRcvdBytes = _ConnRTCRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 13),
    _ConnRTCRcvdBytes_Type()
)
connRTCRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdBytes.setStatus("mandatory")
_ConnRTCRcvdBytesDiscarded_Type = Counter32
_ConnRTCRcvdBytesDiscarded_Object = MibTableColumn
connRTCRcvdBytesDiscarded = _ConnRTCRcvdBytesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 14),
    _ConnRTCRcvdBytesDiscarded_Type()
)
connRTCRcvdBytesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRcvdBytesDiscarded.setStatus("mandatory")
_ConnRTCXmitBytes_Type = Counter32
_ConnRTCXmitBytes_Object = MibTableColumn
connRTCXmitBytes = _ConnRTCXmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 15),
    _ConnRTCXmitBytes_Type()
)
connRTCXmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitBytes.setStatus("mandatory")
_ConnRTCXmitBytesDiscarded_Type = Counter32
_ConnRTCXmitBytesDiscarded_Object = MibTableColumn
connRTCXmitBytesDiscarded = _ConnRTCXmitBytesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 16),
    _ConnRTCXmitBytesDiscarded_Type()
)
connRTCXmitBytesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitBytesDiscarded.setStatus("mandatory")
_ConnRTCSecondsV25ModemOn_Type = Counter32
_ConnRTCSecondsV25ModemOn_Object = MibTableColumn
connRTCSecondsV25ModemOn = _ConnRTCSecondsV25ModemOn_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 17),
    _ConnRTCSecondsV25ModemOn_Type()
)
connRTCSecondsV25ModemOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCSecondsV25ModemOn.setStatus("mandatory")
_ConnRTCSecondsDsiEnabled_Type = Counter32
_ConnRTCSecondsDsiEnabled_Object = MibTableColumn
connRTCSecondsDsiEnabled = _ConnRTCSecondsDsiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 18),
    _ConnRTCSecondsDsiEnabled_Type()
)
connRTCSecondsDsiEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCSecondsDsiEnabled.setStatus("mandatory")
_ConnRTCSecondsOffHook_Type = Counter32
_ConnRTCSecondsOffHook_Object = MibTableColumn
connRTCSecondsOffHook = _ConnRTCSecondsOffHook_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 19),
    _ConnRTCSecondsOffHook_Type()
)
connRTCSecondsOffHook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCSecondsOffHook.setStatus("mandatory")
_ConnRTCSecondsInService_Type = Counter32
_ConnRTCSecondsInService_Object = MibTableColumn
connRTCSecondsInService = _ConnRTCSecondsInService_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 20),
    _ConnRTCSecondsInService_Type()
)
connRTCSecondsInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCSecondsInService.setStatus("mandatory")
_ConnRTCXmitFramesWithFECN_Type = Counter32
_ConnRTCXmitFramesWithFECN_Object = MibTableColumn
connRTCXmitFramesWithFECN = _ConnRTCXmitFramesWithFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 21),
    _ConnRTCXmitFramesWithFECN_Type()
)
connRTCXmitFramesWithFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitFramesWithFECN.setStatus("mandatory")
_ConnRTCXmitFramesWithBECN_Type = Counter32
_ConnRTCXmitFramesWithBECN_Object = MibTableColumn
connRTCXmitFramesWithBECN = _ConnRTCXmitFramesWithBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 22),
    _ConnRTCXmitFramesWithBECN_Type()
)
connRTCXmitFramesWithBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCXmitFramesWithBECN.setStatus("mandatory")
_ConnRTCRxSupervisoryPkts_Type = Counter32
_ConnRTCRxSupervisoryPkts_Object = MibTableColumn
connRTCRxSupervisoryPkts = _ConnRTCRxSupervisoryPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 23),
    _ConnRTCRxSupervisoryPkts_Type()
)
connRTCRxSupervisoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCRxSupervisoryPkts.setStatus("mandatory")
_ConnRTCCongestedMinuites_Type = Counter32
_ConnRTCCongestedMinuites_Object = MibTableColumn
connRTCCongestedMinuites = _ConnRTCCongestedMinuites_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 24),
    _ConnRTCCongestedMinuites_Type()
)
connRTCCongestedMinuites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCCongestedMinuites.setStatus("mandatory")
_ConnRTCFramesRxWithDE_Type = Counter32
_ConnRTCFramesRxWithDE_Object = MibTableColumn
connRTCFramesRxWithDE = _ConnRTCFramesRxWithDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 25),
    _ConnRTCFramesRxWithDE_Type()
)
connRTCFramesRxWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCFramesRxWithDE.setStatus("mandatory")
_ConnRTCFramesTxWithDE_Type = Counter32
_ConnRTCFramesTxWithDE_Object = MibTableColumn
connRTCFramesTxWithDE = _ConnRTCFramesTxWithDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 26),
    _ConnRTCFramesTxWithDE_Type()
)
connRTCFramesTxWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCFramesTxWithDE.setStatus("mandatory")
_ConnRTCFramesDiscardedWithDE_Type = Counter32
_ConnRTCFramesDiscardedWithDE_Object = MibTableColumn
connRTCFramesDiscardedWithDE = _ConnRTCFramesDiscardedWithDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 27),
    _ConnRTCFramesDiscardedWithDE_Type()
)
connRTCFramesDiscardedWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCFramesDiscardedWithDE.setStatus("mandatory")
_ConnRTCBytesRxWithDE_Type = Counter32
_ConnRTCBytesRxWithDE_Object = MibTableColumn
connRTCBytesRxWithDE = _ConnRTCBytesRxWithDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 28),
    _ConnRTCBytesRxWithDE_Type()
)
connRTCBytesRxWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCBytesRxWithDE.setStatus("mandatory")
_ConnRTCFramesRxExcessCir_Type = Counter32
_ConnRTCFramesRxExcessCir_Object = MibTableColumn
connRTCFramesRxExcessCir = _ConnRTCFramesRxExcessCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 29),
    _ConnRTCFramesRxExcessCir_Type()
)
connRTCFramesRxExcessCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCFramesRxExcessCir.setStatus("mandatory")
_ConnRTCBytesRxExcessCir_Type = Counter32
_ConnRTCBytesRxExcessCir_Object = MibTableColumn
connRTCBytesRxExcessCir = _ConnRTCBytesRxExcessCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 30),
    _ConnRTCBytesRxExcessCir_Type()
)
connRTCBytesRxExcessCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCBytesRxExcessCir.setStatus("mandatory")
_ConnRTCFramesTxExcessCir_Type = Counter32
_ConnRTCFramesTxExcessCir_Object = MibScalar
connRTCFramesTxExcessCir = _ConnRTCFramesTxExcessCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 31),
    _ConnRTCFramesTxExcessCir_Type()
)
connRTCFramesTxExcessCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCFramesTxExcessCir.setStatus("mandatory")
_ConnRTCBytesTxExcessCir_Type = Counter32
_ConnRTCBytesTxExcessCir_Object = MibScalar
connRTCBytesTxExcessCir = _ConnRTCBytesTxExcessCir_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 32),
    _ConnRTCBytesTxExcessCir_Type()
)
connRTCBytesTxExcessCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCBytesTxExcessCir.setStatus("mandatory")
_ConnRTCLine_Type = Integer32
_ConnRTCLine_Object = MibTableColumn
connRTCLine = _ConnRTCLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 4, 1, 33),
    _ConnRTCLine_Type()
)
connRTCLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRTCLine.setStatus("mandatory")
_TrunkRTCTable_Object = MibTable
trunkRTCTable = _TrunkRTCTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5)
)
if mibBuilder.loadTexts:
    trunkRTCTable.setStatus("mandatory")
_TrunkRTCEntry_Object = MibTableRow
trunkRTCEntry = _TrunkRTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1)
)
trunkRTCEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "trunkRTCLocalSlot"),
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "trunkRTCLocalPort"),
)
if mibBuilder.loadTexts:
    trunkRTCEntry.setStatus("mandatory")
_TrunkRTCLocalSlot_Type = Integer32
_TrunkRTCLocalSlot_Object = MibTableColumn
trunkRTCLocalSlot = _TrunkRTCLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 1),
    _TrunkRTCLocalSlot_Type()
)
trunkRTCLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCLocalSlot.setStatus("mandatory")
_TrunkRTCLocalPort_Type = Integer32
_TrunkRTCLocalPort_Object = MibTableColumn
trunkRTCLocalPort = _TrunkRTCLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 2),
    _TrunkRTCLocalPort_Type()
)
trunkRTCLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCLocalPort.setStatus("mandatory")
_TrunkRTCBipolarViolations_Type = Counter32
_TrunkRTCBipolarViolations_Object = MibTableColumn
trunkRTCBipolarViolations = _TrunkRTCBipolarViolations_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 4),
    _TrunkRTCBipolarViolations_Type()
)
trunkRTCBipolarViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBipolarViolations.setStatus("mandatory")
_TrunkRTCFrameSlips_Type = Counter32
_TrunkRTCFrameSlips_Object = MibTableColumn
trunkRTCFrameSlips = _TrunkRTCFrameSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 5),
    _TrunkRTCFrameSlips_Type()
)
trunkRTCFrameSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCFrameSlips.setStatus("mandatory")
_TrunkRTCOutOfFrames_Type = Counter32
_TrunkRTCOutOfFrames_Object = MibTableColumn
trunkRTCOutOfFrames = _TrunkRTCOutOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 6),
    _TrunkRTCOutOfFrames_Type()
)
trunkRTCOutOfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCOutOfFrames.setStatus("mandatory")
_TrunkRTCLossOfSignal_Type = Counter32
_TrunkRTCLossOfSignal_Object = MibTableColumn
trunkRTCLossOfSignal = _TrunkRTCLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 7),
    _TrunkRTCLossOfSignal_Type()
)
trunkRTCLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCLossOfSignal.setStatus("mandatory")
_TrunkRTCFrameBitErrors_Type = Counter32
_TrunkRTCFrameBitErrors_Object = MibTableColumn
trunkRTCFrameBitErrors = _TrunkRTCFrameBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 8),
    _TrunkRTCFrameBitErrors_Type()
)
trunkRTCFrameBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCFrameBitErrors.setStatus("mandatory")
_TrunkRTCCrcErrors_Type = Counter32
_TrunkRTCCrcErrors_Object = MibTableColumn
trunkRTCCrcErrors = _TrunkRTCCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 9),
    _TrunkRTCCrcErrors_Type()
)
trunkRTCCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCCrcErrors.setStatus("mandatory")
_TrunkRTCPktOutOfFrames_Type = Counter32
_TrunkRTCPktOutOfFrames_Object = MibTableColumn
trunkRTCPktOutOfFrames = _TrunkRTCPktOutOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 10),
    _TrunkRTCPktOutOfFrames_Type()
)
trunkRTCPktOutOfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCPktOutOfFrames.setStatus("mandatory")
_TrunkRTCPktCrcErrors_Type = Counter32
_TrunkRTCPktCrcErrors_Object = MibTableColumn
trunkRTCPktCrcErrors = _TrunkRTCPktCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 11),
    _TrunkRTCPktCrcErrors_Type()
)
trunkRTCPktCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCPktCrcErrors.setStatus("mandatory")
_TrunkRTCBadClockErrors_Type = Counter32
_TrunkRTCBadClockErrors_Object = MibTableColumn
trunkRTCBadClockErrors = _TrunkRTCBadClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 12),
    _TrunkRTCBadClockErrors_Type()
)
trunkRTCBadClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBadClockErrors.setStatus("mandatory")
_TrunkRTCVoicePktsDropped_Type = Counter32
_TrunkRTCVoicePktsDropped_Object = MibTableColumn
trunkRTCVoicePktsDropped = _TrunkRTCVoicePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 13),
    _TrunkRTCVoicePktsDropped_Type()
)
trunkRTCVoicePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCVoicePktsDropped.setStatus("mandatory")
_TrunkRTCTimeStampedPktsDropped_Type = Counter32
_TrunkRTCTimeStampedPktsDropped_Object = MibTableColumn
trunkRTCTimeStampedPktsDropped = _TrunkRTCTimeStampedPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 14),
    _TrunkRTCTimeStampedPktsDropped_Type()
)
trunkRTCTimeStampedPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTimeStampedPktsDropped.setStatus("mandatory")
_TrunkRTCNonTimeStampedPktsDropped_Type = Counter32
_TrunkRTCNonTimeStampedPktsDropped_Object = MibTableColumn
trunkRTCNonTimeStampedPktsDropped = _TrunkRTCNonTimeStampedPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 15),
    _TrunkRTCNonTimeStampedPktsDropped_Type()
)
trunkRTCNonTimeStampedPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCNonTimeStampedPktsDropped.setStatus("mandatory")
_TrunkRTCHighPriorityPktsDropped_Type = Counter32
_TrunkRTCHighPriorityPktsDropped_Object = MibTableColumn
trunkRTCHighPriorityPktsDropped = _TrunkRTCHighPriorityPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 16),
    _TrunkRTCHighPriorityPktsDropped_Type()
)
trunkRTCHighPriorityPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCHighPriorityPktsDropped.setStatus("mandatory")
_TrunkRTCBurstyDataPktsDropped_Type = Counter32
_TrunkRTCBurstyDataPktsDropped_Object = MibTableColumn
trunkRTCBurstyDataPktsDropped = _TrunkRTCBurstyDataPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 17),
    _TrunkRTCBurstyDataPktsDropped_Type()
)
trunkRTCBurstyDataPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataPktsDropped.setStatus("mandatory")
_TrunkRTCMulticastPktsDropped_Type = Counter32
_TrunkRTCMulticastPktsDropped_Object = MibTableColumn
trunkRTCMulticastPktsDropped = _TrunkRTCMulticastPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 18),
    _TrunkRTCMulticastPktsDropped_Type()
)
trunkRTCMulticastPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCMulticastPktsDropped.setStatus("mandatory")
_TrunkRTCVoicePktsXmitted_Type = Counter32
_TrunkRTCVoicePktsXmitted_Object = MibTableColumn
trunkRTCVoicePktsXmitted = _TrunkRTCVoicePktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 19),
    _TrunkRTCVoicePktsXmitted_Type()
)
trunkRTCVoicePktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCVoicePktsXmitted.setStatus("mandatory")
_TrunkRTCTimeStampedPktsXmitted_Type = Counter32
_TrunkRTCTimeStampedPktsXmitted_Object = MibTableColumn
trunkRTCTimeStampedPktsXmitted = _TrunkRTCTimeStampedPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 20),
    _TrunkRTCTimeStampedPktsXmitted_Type()
)
trunkRTCTimeStampedPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTimeStampedPktsXmitted.setStatus("mandatory")
_TrunkRTCNonTimeStampedPktsXmitted_Type = Counter32
_TrunkRTCNonTimeStampedPktsXmitted_Object = MibTableColumn
trunkRTCNonTimeStampedPktsXmitted = _TrunkRTCNonTimeStampedPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 21),
    _TrunkRTCNonTimeStampedPktsXmitted_Type()
)
trunkRTCNonTimeStampedPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCNonTimeStampedPktsXmitted.setStatus("mandatory")
_TrunkRTCHighPriorityPktsXmitted_Type = Counter32
_TrunkRTCHighPriorityPktsXmitted_Object = MibTableColumn
trunkRTCHighPriorityPktsXmitted = _TrunkRTCHighPriorityPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 22),
    _TrunkRTCHighPriorityPktsXmitted_Type()
)
trunkRTCHighPriorityPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCHighPriorityPktsXmitted.setStatus("mandatory")
_TrunkRTCBurstyDataPktsXmitted_Type = Counter32
_TrunkRTCBurstyDataPktsXmitted_Object = MibTableColumn
trunkRTCBurstyDataPktsXmitted = _TrunkRTCBurstyDataPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 23),
    _TrunkRTCBurstyDataPktsXmitted_Type()
)
trunkRTCBurstyDataPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataPktsXmitted.setStatus("mandatory")
_TrunkRTCMulticastPktsXmitted_Type = Counter32
_TrunkRTCMulticastPktsXmitted_Object = MibTableColumn
trunkRTCMulticastPktsXmitted = _TrunkRTCMulticastPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 24),
    _TrunkRTCMulticastPktsXmitted_Type()
)
trunkRTCMulticastPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCMulticastPktsXmitted.setStatus("mandatory")
_TrunkRTCPktsXmitted_Type = Counter32
_TrunkRTCPktsXmitted_Object = MibTableColumn
trunkRTCPktsXmitted = _TrunkRTCPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 25),
    _TrunkRTCPktsXmitted_Type()
)
trunkRTCPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCPktsXmitted.setStatus("mandatory")
_TrunkRTCTxBurstyDataAClpPktsDropped_Type = Counter32
_TrunkRTCTxBurstyDataAClpPktsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataAClpPktsDropped = _TrunkRTCTxBurstyDataAClpPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 26),
    _TrunkRTCTxBurstyDataAClpPktsDropped_Type()
)
trunkRTCTxBurstyDataAClpPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataAClpPktsDropped.setStatus("mandatory")
_TrunkRTCTxBurstyDataBClpPktsDropped_Type = Counter32
_TrunkRTCTxBurstyDataBClpPktsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataBClpPktsDropped = _TrunkRTCTxBurstyDataBClpPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 27),
    _TrunkRTCTxBurstyDataBClpPktsDropped_Type()
)
trunkRTCTxBurstyDataBClpPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataBClpPktsDropped.setStatus("mandatory")
_TrunkRTCBurstyDataAEfcnPktsTx2Line_Type = Counter32
_TrunkRTCBurstyDataAEfcnPktsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataAEfcnPktsTx2Line = _TrunkRTCBurstyDataAEfcnPktsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 28),
    _TrunkRTCBurstyDataAEfcnPktsTx2Line_Type()
)
trunkRTCBurstyDataAEfcnPktsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataAEfcnPktsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataBEfcnPktsTx2Line_Type = Counter32
_TrunkRTCBurstyDataBEfcnPktsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataBEfcnPktsTx2Line = _TrunkRTCBurstyDataBEfcnPktsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 29),
    _TrunkRTCBurstyDataBEfcnPktsTx2Line_Type()
)
trunkRTCBurstyDataBEfcnPktsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataBEfcnPktsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataAClpPktsTx2Line_Type = Counter32
_TrunkRTCBurstyDataAClpPktsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataAClpPktsTx2Line = _TrunkRTCBurstyDataAClpPktsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 30),
    _TrunkRTCBurstyDataAClpPktsTx2Line_Type()
)
trunkRTCBurstyDataAClpPktsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataAClpPktsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataBClpPktsTx2Line_Type = Counter32
_TrunkRTCBurstyDataBClpPktsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataBClpPktsTx2Line = _TrunkRTCBurstyDataBClpPktsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 31),
    _TrunkRTCBurstyDataBClpPktsTx2Line_Type()
)
trunkRTCBurstyDataBClpPktsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataBClpPktsTx2Line.setStatus("mandatory")
_TrunkRTCAtmCellHeaderHecErrors_Type = Counter32
_TrunkRTCAtmCellHeaderHecErrors_Object = MibTableColumn
trunkRTCAtmCellHeaderHecErrors = _TrunkRTCAtmCellHeaderHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 32),
    _TrunkRTCAtmCellHeaderHecErrors_Type()
)
trunkRTCAtmCellHeaderHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCAtmCellHeaderHecErrors.setStatus("mandatory")
_TrunkRTCTxVoiceCellsDropped_Type = Counter32
_TrunkRTCTxVoiceCellsDropped_Object = MibTableColumn
trunkRTCTxVoiceCellsDropped = _TrunkRTCTxVoiceCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 33),
    _TrunkRTCTxVoiceCellsDropped_Type()
)
trunkRTCTxVoiceCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxVoiceCellsDropped.setStatus("mandatory")
_TrunkRTCTxTimeStampCellsDropped_Type = Counter32
_TrunkRTCTxTimeStampCellsDropped_Object = MibTableColumn
trunkRTCTxTimeStampCellsDropped = _TrunkRTCTxTimeStampCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 34),
    _TrunkRTCTxTimeStampCellsDropped_Type()
)
trunkRTCTxTimeStampCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxTimeStampCellsDropped.setStatus("mandatory")
_TrunkRTCTxNonTStampCellsDropped_Type = Counter32
_TrunkRTCTxNonTStampCellsDropped_Object = MibTableColumn
trunkRTCTxNonTStampCellsDropped = _TrunkRTCTxNonTStampCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 35),
    _TrunkRTCTxNonTStampCellsDropped_Type()
)
trunkRTCTxNonTStampCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxNonTStampCellsDropped.setStatus("mandatory")
_TrunkRTCTxHighPriorityCellsDropped_Type = Counter32
_TrunkRTCTxHighPriorityCellsDropped_Object = MibTableColumn
trunkRTCTxHighPriorityCellsDropped = _TrunkRTCTxHighPriorityCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 36),
    _TrunkRTCTxHighPriorityCellsDropped_Type()
)
trunkRTCTxHighPriorityCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxHighPriorityCellsDropped.setStatus("mandatory")
_TrunkRTCTxBurstyDataACellsDropped_Type = Counter32
_TrunkRTCTxBurstyDataACellsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataACellsDropped = _TrunkRTCTxBurstyDataACellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 37),
    _TrunkRTCTxBurstyDataACellsDropped_Type()
)
trunkRTCTxBurstyDataACellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataACellsDropped.setStatus("mandatory")
_TrunkRTCTxBurstyDataBCellsDropped_Type = Counter32
_TrunkRTCTxBurstyDataBCellsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataBCellsDropped = _TrunkRTCTxBurstyDataBCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 38),
    _TrunkRTCTxBurstyDataBCellsDropped_Type()
)
trunkRTCTxBurstyDataBCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataBCellsDropped.setStatus("mandatory")
_TrunkRTCVoiceCellsTx2Line_Type = Counter32
_TrunkRTCVoiceCellsTx2Line_Object = MibTableColumn
trunkRTCVoiceCellsTx2Line = _TrunkRTCVoiceCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 39),
    _TrunkRTCVoiceCellsTx2Line_Type()
)
trunkRTCVoiceCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCVoiceCellsTx2Line.setStatus("mandatory")
_TrunkRTCTimeStampCellsTx2Line_Type = Counter32
_TrunkRTCTimeStampCellsTx2Line_Object = MibTableColumn
trunkRTCTimeStampCellsTx2Line = _TrunkRTCTimeStampCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 40),
    _TrunkRTCTimeStampCellsTx2Line_Type()
)
trunkRTCTimeStampCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTimeStampCellsTx2Line.setStatus("mandatory")
_TrunkRTCNonTimeStampCellsTx2Line_Type = Counter32
_TrunkRTCNonTimeStampCellsTx2Line_Object = MibTableColumn
trunkRTCNonTimeStampCellsTx2Line = _TrunkRTCNonTimeStampCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 41),
    _TrunkRTCNonTimeStampCellsTx2Line_Type()
)
trunkRTCNonTimeStampCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCNonTimeStampCellsTx2Line.setStatus("mandatory")
_TrunkRTCHighPriorityCellsTx2Line_Type = Counter32
_TrunkRTCHighPriorityCellsTx2Line_Object = MibTableColumn
trunkRTCHighPriorityCellsTx2Line = _TrunkRTCHighPriorityCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 42),
    _TrunkRTCHighPriorityCellsTx2Line_Type()
)
trunkRTCHighPriorityCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCHighPriorityCellsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataACellsTx2Line_Type = Counter32
_TrunkRTCBurstyDataACellsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataACellsTx2Line = _TrunkRTCBurstyDataACellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 43),
    _TrunkRTCBurstyDataACellsTx2Line_Type()
)
trunkRTCBurstyDataACellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataACellsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataBCellsTx2Line_Type = Counter32
_TrunkRTCBurstyDataBCellsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataBCellsTx2Line = _TrunkRTCBurstyDataBCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 44),
    _TrunkRTCBurstyDataBCellsTx2Line_Type()
)
trunkRTCBurstyDataBCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataBCellsTx2Line.setStatus("mandatory")
_TrunkRTCTotalCellsTx2Line_Type = Counter32
_TrunkRTCTotalCellsTx2Line_Object = MibTableColumn
trunkRTCTotalCellsTx2Line = _TrunkRTCTotalCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 45),
    _TrunkRTCTotalCellsTx2Line_Type()
)
trunkRTCTotalCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTotalCellsTx2Line.setStatus("mandatory")
_TrunkRTCTxBurstyDataAClpCellsDropped_Type = Counter32
_TrunkRTCTxBurstyDataAClpCellsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataAClpCellsDropped = _TrunkRTCTxBurstyDataAClpCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 46),
    _TrunkRTCTxBurstyDataAClpCellsDropped_Type()
)
trunkRTCTxBurstyDataAClpCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataAClpCellsDropped.setStatus("mandatory")
_TrunkRTCTxBurstyDataBClpCellsDropped_Type = Counter32
_TrunkRTCTxBurstyDataBClpCellsDropped_Object = MibTableColumn
trunkRTCTxBurstyDataBClpCellsDropped = _TrunkRTCTxBurstyDataBClpCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 47),
    _TrunkRTCTxBurstyDataBClpCellsDropped_Type()
)
trunkRTCTxBurstyDataBClpCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCTxBurstyDataBClpCellsDropped.setStatus("mandatory")
_TrunkRTCBurstyDataAEfcnCellsTx2Line_Type = Counter32
_TrunkRTCBurstyDataAEfcnCellsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataAEfcnCellsTx2Line = _TrunkRTCBurstyDataAEfcnCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 48),
    _TrunkRTCBurstyDataAEfcnCellsTx2Line_Type()
)
trunkRTCBurstyDataAEfcnCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataAEfcnCellsTx2Line.setStatus("mandatory")
_TrunkRTCBurstyDataBEfcnCellsTx2Line_Type = Counter32
_TrunkRTCBurstyDataBEfcnCellsTx2Line_Object = MibTableColumn
trunkRTCBurstyDataBEfcnCellsTx2Line = _TrunkRTCBurstyDataBEfcnCellsTx2Line_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 49),
    _TrunkRTCBurstyDataBEfcnCellsTx2Line_Type()
)
trunkRTCBurstyDataBEfcnCellsTx2Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCBurstyDataBEfcnCellsTx2Line.setStatus("mandatory")
_TrunkRTCPlcpOutOfFrames_Type = Counter32
_TrunkRTCPlcpOutOfFrames_Object = MibTableColumn
trunkRTCPlcpOutOfFrames = _TrunkRTCPlcpOutOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 2, 6, 5, 1, 50),
    _TrunkRTCPlcpOutOfFrames_Type()
)
trunkRTCPlcpOutOfFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkRTCPlcpOutOfFrames.setStatus("mandatory")
_Rtm_ObjectIdentity = ObjectIdentity
rtm = _Rtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 120)
)
_TrapsConfig_ObjectIdentity = ObjectIdentity
trapsConfig = _TrapsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 120, 1)
)
_TrapConfigTable_Object = MibTable
trapConfigTable = _TrapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1)
)
if mibBuilder.loadTexts:
    trapConfigTable.setStatus("mandatory")
_TrapConfigEntry_Object = MibTableRow
trapConfigEntry = _TrapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1)
)
trapConfigEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "managerIPaddress"),
)
if mibBuilder.loadTexts:
    trapConfigEntry.setStatus("mandatory")
_ManagerIPaddress_Type = IpAddress
_ManagerIPaddress_Object = MibTableColumn
managerIPaddress = _ManagerIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 1),
    _ManagerIPaddress_Type()
)
managerIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIPaddress.setStatus("mandatory")
_ManagerPortNumber_Type = Integer32
_ManagerPortNumber_Object = MibTableColumn
managerPortNumber = _ManagerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 2),
    _ManagerPortNumber_Type()
)
managerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerPortNumber.setStatus("mandatory")


class _ManagerRowStatus_Type(Integer32):
    """Custom type managerRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addRow", 1),
          ("delRow", 2))
    )


_ManagerRowStatus_Type.__name__ = "Integer32"
_ManagerRowStatus_Object = MibTableColumn
managerRowStatus = _ManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 3),
    _ManagerRowStatus_Type()
)
managerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerRowStatus.setStatus("mandatory")


class _ReadingTrapFlag_Type(Integer32):
    """Custom type readingTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ReadingTrapFlag_Type.__name__ = "Integer32"
_ReadingTrapFlag_Object = MibTableColumn
readingTrapFlag = _ReadingTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 4),
    _ReadingTrapFlag_Type()
)
readingTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readingTrapFlag.setStatus("mandatory")
_NextTrapSeqNum_Type = Integer32
_NextTrapSeqNum_Object = MibTableColumn
nextTrapSeqNum = _NextTrapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 5),
    _NextTrapSeqNum_Type()
)
nextTrapSeqNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextTrapSeqNum.setStatus("mandatory")


class _ManagerNumOfValidEntries_Type(Integer32):
    """Custom type managerNumOfValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ManagerNumOfValidEntries_Type.__name__ = "Integer32"
_ManagerNumOfValidEntries_Object = MibScalar
managerNumOfValidEntries = _ManagerNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 2),
    _ManagerNumOfValidEntries_Type()
)
managerNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managerNumOfValidEntries.setStatus("mandatory")
_LastSequenceNumber_Type = Integer32
_LastSequenceNumber_Object = MibScalar
lastSequenceNumber = _LastSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 3),
    _LastSequenceNumber_Type()
)
lastSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSequenceNumber.setStatus("mandatory")
_TrapUploadTable_Object = MibTable
trapUploadTable = _TrapUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4)
)
if mibBuilder.loadTexts:
    trapUploadTable.setStatus("mandatory")
_TrapUploadEntry_Object = MibTableRow
trapUploadEntry = _TrapUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1)
)
trapUploadEntry.setIndexNames(
    (0, "STRATACOM-STRATAVIEW-SVPLUS-MIB", "mgrIpAddress"),
)
if mibBuilder.loadTexts:
    trapUploadEntry.setStatus("mandatory")
_MgrIpAddress_Type = IpAddress
_MgrIpAddress_Object = MibTableColumn
mgrIpAddress = _MgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 1),
    _MgrIpAddress_Type()
)
mgrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgrIpAddress.setStatus("mandatory")
_TrapSequenceNum_Type = Integer32
_TrapSequenceNum_Object = MibTableColumn
trapSequenceNum = _TrapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 2),
    _TrapSequenceNum_Type()
)
trapSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSequenceNum.setStatus("mandatory")
_TrapPduString_Type = OctetString
_TrapPduString_Object = MibTableColumn
trapPduString = _TrapPduString_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 3),
    _TrapPduString_Type()
)
trapPduString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPduString.setStatus("mandatory")


class _EndOfQueueFlag_Type(Integer32):
    """Custom type endOfQueueFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_EndOfQueueFlag_Type.__name__ = "Integer32"
_EndOfQueueFlag_Object = MibTableColumn
endOfQueueFlag = _EndOfQueueFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 4),
    _EndOfQueueFlag_Type()
)
endOfQueueFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfQueueFlag.setStatus("mandatory")
_StrataviewEvents_ObjectIdentity = ObjectIdentity
strataviewEvents = _StrataviewEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 920)
)

# Managed Objects groups


# Notification objects

filteredLogRecord = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 1, 0, 0)
)
filteredLogRecord.setObjects(
      *(("STRATACOM-STRATAVIEW-SVPLUS-MIB", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "logIndex"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "logNetwork"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "logNodeName"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "logGmtDate"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "logSeverity"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "logMsg"))
)
if mibBuilder.loadTexts:
    filteredLogRecord.setStatus(
        ""
    )

trunkStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 2, 0, 0)
)
trunkStatusAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-SVPLUS-MIB", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "nodeGrpName"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "nodeGrpNetName"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "trunkStatus"))
)
if mibBuilder.loadTexts:
    trunkStatusAlarm.setStatus(
        ""
    )

cirLineStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 2, 0, 1)
)
cirLineStatusAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-SVPLUS-MIB", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "nodeGrpName"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "nodeGrpNetName"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "cirLineStatus"))
)
if mibBuilder.loadTexts:
    cirLineStatusAlarm.setStatus(
        ""
    )

frpStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 2, 0, 2)
)
frpStatusAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-SVPLUS-MIB", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "nodeGrpName"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "nodeGrpNetName"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "frpStatus"))
)
if mibBuilder.loadTexts:
    frpStatusAlarm.setStatus(
        ""
    )

connStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 2, 0, 3)
)
connStatusAlarm.setObjects(
      *(("STRATACOM-STRATAVIEW-SVPLUS-MIB", "lastSequenceNumber"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "nodeGrpName"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "nodeGrpNetName"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "connStatus"),
        ("STRATACOM-STRATAVIEW-SVPLUS-MIB", "connABitStatus"))
)
if mibBuilder.loadTexts:
    connStatusAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STRATACOM-STRATAVIEW-SVPLUS-MIB",
    **{"Active": Active,
       "Severity": Severity,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "stratacom": stratacom,
       "svplus": svplus,
       "filteredLogRecord": filteredLogRecord,
       "controlGroup": controlGroup,
       "databaseSampleFreq": databaseSampleFreq,
       "logGroup": logGroup,
       "currentMaxLogIndex": currentMaxLogIndex,
       "maintLogTable": maintLogTable,
       "maintLogEntry": maintLogEntry,
       "logIndex": logIndex,
       "logNetwork": logNetwork,
       "logNodeName": logNodeName,
       "logGmtDate": logGmtDate,
       "logSeverity": logSeverity,
       "logMsg": logMsg,
       "eventFilterTable": eventFilterTable,
       "eventFilterEntry": eventFilterEntry,
       "eventFilterIndex": eventFilterIndex,
       "eventFilterStatus": eventFilterStatus,
       "eventFilterSeverity": eventFilterSeverity,
       "eventFilterSubstring": eventFilterSubstring,
       "maintLogFilterGroup": maintLogFilterGroup,
       "maintLogFilterTimeMin": maintLogFilterTimeMin,
       "maintLogFilterTimeMax": maintLogFilterTimeMax,
       "maintLogFilterWindow": maintLogFilterWindow,
       "maintLogFilterNetworkNam": maintLogFilterNetworkNam,
       "maintLogFilterNodeName": maintLogFilterNodeName,
       "maintLogFilterSeverity": maintLogFilterSeverity,
       "networkGroup": networkGroup,
       "networkTable": networkTable,
       "networkEntry": networkEntry,
       "networkName": networkName,
       "networkId": networkId,
       "networkIpxId": networkIpxId,
       "nodeGroup": nodeGroup,
       "nodeTable": nodeTable,
       "nodeEntry": nodeEntry,
       "nodeNetworkName": nodeNetworkName,
       "nodeName": nodeName,
       "svnode": svnode,
       "trunkStatusAlarm": trunkStatusAlarm,
       "cirLineStatusAlarm": cirLineStatusAlarm,
       "frpStatusAlarm": frpStatusAlarm,
       "connStatusAlarm": connStatusAlarm,
       "svNodeGroup": svNodeGroup,
       "nodeGrpName": nodeGrpName,
       "nodeGrpNetName": nodeGrpNetName,
       "nodeGrpAlarmState": nodeGrpAlarmState,
       "nodeGrpGateway": nodeGrpGateway,
       "nodeGrpActive": nodeGrpActive,
       "nodeGrpPlatform": nodeGrpPlatform,
       "nodeGrpRelease": nodeGrpRelease,
       "nodeFsIncRate": nodeFsIncRate,
       "nodeFsDecRate": nodeFsDecRate,
       "nodeFsFastRate": nodeFsFastRate,
       "nodeRstTimeout": nodeRstTimeout,
       "alarmTrapSequenceNumber": alarmTrapSequenceNumber,
       "packetGroup": packetGroup,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkLocalSlot": trunkLocalSlot,
       "trunkLocalPort": trunkLocalPort,
       "trunkLocalLine": trunkLocalLine,
       "trunkCardType": trunkCardType,
       "trunkInterface": trunkInterface,
       "trunkLineLoad": trunkLineLoad,
       "trunkRemNodeId": trunkRemNodeId,
       "trunkRemLineNumber": trunkRemLineNumber,
       "trunkRemSlot": trunkRemSlot,
       "trunkRemPort": trunkRemPort,
       "trunkAlarmState": trunkAlarmState,
       "trunkComment": trunkComment,
       "trunkActive": trunkActive,
       "trunkStatus": trunkStatus,
       "trunkStatReserve": trunkStatReserve,
       "trunkBurstyDataBQDepth": trunkBurstyDataBQDepth,
       "trunkBurstyDataBQEfcnThreshold": trunkBurstyDataBQEfcnThreshold,
       "trunkClpHighDropThreshold": trunkClpHighDropThreshold,
       "trunkClpLowDropThreshold": trunkClpLowDropThreshold,
       "circuitGroup": circuitGroup,
       "cirLineTable": cirLineTable,
       "cirLineEntry": cirLineEntry,
       "cirLineLineNumber": cirLineLineNumber,
       "cirLineCardType": cirLineCardType,
       "cirLineInterface": cirLineInterface,
       "cirLineComment": cirLineComment,
       "cirLineActive": cirLineActive,
       "cirLineStatus": cirLineStatus,
       "frpGroup": frpGroup,
       "frpTable": frpTable,
       "frpEntry": frpEntry,
       "frpLocalSlot": frpLocalSlot,
       "frpLocalPort": frpLocalPort,
       "frpPortSpeed": frpPortSpeed,
       "frpComment": frpComment,
       "frpActive": frpActive,
       "frpStatus": frpStatus,
       "frpQDepth": frpQDepth,
       "frpEcnThreshold": frpEcnThreshold,
       "frpDeThreshold": frpDeThreshold,
       "frpPortType": frpPortType,
       "frpLocalLine": frpLocalLine,
       "connGroup": connGroup,
       "connTable": connTable,
       "connEntry": connEntry,
       "connLocalSlot": connLocalSlot,
       "connLocalChannel": connLocalChannel,
       "connLocalDLCI": connLocalDLCI,
       "connRemoteNodeId": connRemoteNodeId,
       "connRemoteSlot": connRemoteSlot,
       "connRemoteChannel": connRemoteChannel,
       "connRemoteDLCI": connRemoteDLCI,
       "connType": connType,
       "connRate": connRate,
       "connLocalMaxPkts": connLocalMaxPkts,
       "connRemoteMaxPkts": connRemoteMaxPkts,
       "connMinBandwidth": connMinBandwidth,
       "connDAX": connDAX,
       "connTXR": connTXR,
       "connComment": connComment,
       "connActive": connActive,
       "connStatus": connStatus,
       "connQir": connQir,
       "connPir": connPir,
       "connVcQueDepth": connVcQueDepth,
       "connVcQueThreshold": connVcQueThreshold,
       "connCMax": connCMax,
       "connPerUtil": connPerUtil,
       "connConnInfoFlag": connConnInfoFlag,
       "connCir": connCir,
       "connABitStatus": connABitStatus,
       "connLocalLine": connLocalLine,
       "realTimeCountersGroup": realTimeCountersGroup,
       "cirLineRTCTable": cirLineRTCTable,
       "cirLineRTCEntry": cirLineRTCEntry,
       "cirLineRTCLineNumber": cirLineRTCLineNumber,
       "cirLineRTCBipolarViolations": cirLineRTCBipolarViolations,
       "cirLineRTCFrameSlips": cirLineRTCFrameSlips,
       "cirLineRTCOutOfFrames": cirLineRTCOutOfFrames,
       "cirLineRTCLossesOfSignal": cirLineRTCLossesOfSignal,
       "cirLineRTCFrameBitErrors": cirLineRTCFrameBitErrors,
       "cirLineRTCCrcErrors": cirLineRTCCrcErrors,
       "cirLineRTCOutOfMultiFrames": cirLineRTCOutOfMultiFrames,
       "cirLineRTCAllOnesInTimeslot16": cirLineRTCAllOnesInTimeslot16,
       "frpRTCTable": frpRTCTable,
       "frpRTCEntry": frpRTCEntry,
       "frpRTCSlot": frpRTCSlot,
       "frpRTCPort": frpRTCPort,
       "frpRTCFramesRcvd": frpRTCFramesRcvd,
       "frpRTCFramesXmitted": frpRTCFramesXmitted,
       "frpRTCBytesRcvd": frpRTCBytesRcvd,
       "frpRTCBytesXmitted": frpRTCBytesXmitted,
       "frpRTCFramesXmittedWithFECN": frpRTCFramesXmittedWithFECN,
       "frpRTCFramesXmittedWithBECN": frpRTCFramesXmittedWithBECN,
       "frpRTCFramesRcvdCrcErrors": frpRTCFramesRcvdCrcErrors,
       "frpRTCFramesRcvdInvalidFormat": frpRTCFramesRcvdInvalidFormat,
       "frpRTCFramesRcvdAlignmentErrors": frpRTCFramesRcvdAlignmentErrors,
       "frpRTCFramesRcvdIllegalLen": frpRTCFramesRcvdIllegalLen,
       "frpRTCDmaOverruns": frpRTCDmaOverruns,
       "frpRTCLmiStatusEnquires": frpRTCLmiStatusEnquires,
       "frpRTCLmiStatusXmitRate": frpRTCLmiStatusXmitRate,
       "frpRTCLmiStatusUpdateRate": frpRTCLmiStatusUpdateRate,
       "frpRTCLmiInvalidStatusEnquires": frpRTCLmiInvalidStatusEnquires,
       "frpRTCLmiLinkTimeoutErrors": frpRTCLmiLinkTimeoutErrors,
       "frpRTCLmiKeepaliveSequenceErrors": frpRTCLmiKeepaliveSequenceErrors,
       "frpRTCFramesRcvdUndefDlciErrors": frpRTCFramesRcvdUndefDlciErrors,
       "frpRTCXmitStatusEnquirey": frpRTCXmitStatusEnquirey,
       "frpRTCRxStatusCounter": frpRTCRxStatusCounter,
       "frpRTCAsyncStatusCounter": frpRTCAsyncStatusCounter,
       "frpRTCBadSequenceNumberCount": frpRTCBadSequenceNumberCount,
       "frpRTCTxProtocolTimeOutCount": frpRTCTxProtocolTimeOutCount,
       "frpRTCCLLMFramesTx": frpRTCCLLMFramesTx,
       "frpRTCCLLMBytesTx": frpRTCCLLMBytesTx,
       "frpRTCCLLMFramesRx": frpRTCCLLMFramesRx,
       "frpRTCCLLMBytes": frpRTCCLLMBytes,
       "frpRTCCLLMFailures": frpRTCCLLMFailures,
       "frpRTCRxDEFramesDiscarded": frpRTCRxDEFramesDiscarded,
       "frpRTCLine": frpRTCLine,
       "connRTCTable": connRTCTable,
       "connRTCEntry": connRTCEntry,
       "connRTCSlot": connRTCSlot,
       "connRTCChannel": connRTCChannel,
       "connRTCDLCI": connRTCDLCI,
       "connRTCRcvdFrames": connRTCRcvdFrames,
       "connRTCRcvdFramesDiscarded": connRTCRcvdFramesDiscarded,
       "connRTCXmitFrames": connRTCXmitFrames,
       "connRTCXmitFramesDiscarded": connRTCXmitFramesDiscarded,
       "connRTCRcvdPkts": connRTCRcvdPkts,
       "connRTCRcvdPktsDiscarded": connRTCRcvdPktsDiscarded,
       "connRTCXmitPkts": connRTCXmitPkts,
       "connRTCXmitPktsProjected": connRTCXmitPktsProjected,
       "connRTCXmitPktsSupervisory": connRTCXmitPktsSupervisory,
       "connRTCRcvdBytes": connRTCRcvdBytes,
       "connRTCRcvdBytesDiscarded": connRTCRcvdBytesDiscarded,
       "connRTCXmitBytes": connRTCXmitBytes,
       "connRTCXmitBytesDiscarded": connRTCXmitBytesDiscarded,
       "connRTCSecondsV25ModemOn": connRTCSecondsV25ModemOn,
       "connRTCSecondsDsiEnabled": connRTCSecondsDsiEnabled,
       "connRTCSecondsOffHook": connRTCSecondsOffHook,
       "connRTCSecondsInService": connRTCSecondsInService,
       "connRTCXmitFramesWithFECN": connRTCXmitFramesWithFECN,
       "connRTCXmitFramesWithBECN": connRTCXmitFramesWithBECN,
       "connRTCRxSupervisoryPkts": connRTCRxSupervisoryPkts,
       "connRTCCongestedMinuites": connRTCCongestedMinuites,
       "connRTCFramesRxWithDE": connRTCFramesRxWithDE,
       "connRTCFramesTxWithDE": connRTCFramesTxWithDE,
       "connRTCFramesDiscardedWithDE": connRTCFramesDiscardedWithDE,
       "connRTCBytesRxWithDE": connRTCBytesRxWithDE,
       "connRTCFramesRxExcessCir": connRTCFramesRxExcessCir,
       "connRTCBytesRxExcessCir": connRTCBytesRxExcessCir,
       "connRTCFramesTxExcessCir": connRTCFramesTxExcessCir,
       "connRTCBytesTxExcessCir": connRTCBytesTxExcessCir,
       "connRTCLine": connRTCLine,
       "trunkRTCTable": trunkRTCTable,
       "trunkRTCEntry": trunkRTCEntry,
       "trunkRTCLocalSlot": trunkRTCLocalSlot,
       "trunkRTCLocalPort": trunkRTCLocalPort,
       "trunkRTCBipolarViolations": trunkRTCBipolarViolations,
       "trunkRTCFrameSlips": trunkRTCFrameSlips,
       "trunkRTCOutOfFrames": trunkRTCOutOfFrames,
       "trunkRTCLossOfSignal": trunkRTCLossOfSignal,
       "trunkRTCFrameBitErrors": trunkRTCFrameBitErrors,
       "trunkRTCCrcErrors": trunkRTCCrcErrors,
       "trunkRTCPktOutOfFrames": trunkRTCPktOutOfFrames,
       "trunkRTCPktCrcErrors": trunkRTCPktCrcErrors,
       "trunkRTCBadClockErrors": trunkRTCBadClockErrors,
       "trunkRTCVoicePktsDropped": trunkRTCVoicePktsDropped,
       "trunkRTCTimeStampedPktsDropped": trunkRTCTimeStampedPktsDropped,
       "trunkRTCNonTimeStampedPktsDropped": trunkRTCNonTimeStampedPktsDropped,
       "trunkRTCHighPriorityPktsDropped": trunkRTCHighPriorityPktsDropped,
       "trunkRTCBurstyDataPktsDropped": trunkRTCBurstyDataPktsDropped,
       "trunkRTCMulticastPktsDropped": trunkRTCMulticastPktsDropped,
       "trunkRTCVoicePktsXmitted": trunkRTCVoicePktsXmitted,
       "trunkRTCTimeStampedPktsXmitted": trunkRTCTimeStampedPktsXmitted,
       "trunkRTCNonTimeStampedPktsXmitted": trunkRTCNonTimeStampedPktsXmitted,
       "trunkRTCHighPriorityPktsXmitted": trunkRTCHighPriorityPktsXmitted,
       "trunkRTCBurstyDataPktsXmitted": trunkRTCBurstyDataPktsXmitted,
       "trunkRTCMulticastPktsXmitted": trunkRTCMulticastPktsXmitted,
       "trunkRTCPktsXmitted": trunkRTCPktsXmitted,
       "trunkRTCTxBurstyDataAClpPktsDropped": trunkRTCTxBurstyDataAClpPktsDropped,
       "trunkRTCTxBurstyDataBClpPktsDropped": trunkRTCTxBurstyDataBClpPktsDropped,
       "trunkRTCBurstyDataAEfcnPktsTx2Line": trunkRTCBurstyDataAEfcnPktsTx2Line,
       "trunkRTCBurstyDataBEfcnPktsTx2Line": trunkRTCBurstyDataBEfcnPktsTx2Line,
       "trunkRTCBurstyDataAClpPktsTx2Line": trunkRTCBurstyDataAClpPktsTx2Line,
       "trunkRTCBurstyDataBClpPktsTx2Line": trunkRTCBurstyDataBClpPktsTx2Line,
       "trunkRTCAtmCellHeaderHecErrors": trunkRTCAtmCellHeaderHecErrors,
       "trunkRTCTxVoiceCellsDropped": trunkRTCTxVoiceCellsDropped,
       "trunkRTCTxTimeStampCellsDropped": trunkRTCTxTimeStampCellsDropped,
       "trunkRTCTxNonTStampCellsDropped": trunkRTCTxNonTStampCellsDropped,
       "trunkRTCTxHighPriorityCellsDropped": trunkRTCTxHighPriorityCellsDropped,
       "trunkRTCTxBurstyDataACellsDropped": trunkRTCTxBurstyDataACellsDropped,
       "trunkRTCTxBurstyDataBCellsDropped": trunkRTCTxBurstyDataBCellsDropped,
       "trunkRTCVoiceCellsTx2Line": trunkRTCVoiceCellsTx2Line,
       "trunkRTCTimeStampCellsTx2Line": trunkRTCTimeStampCellsTx2Line,
       "trunkRTCNonTimeStampCellsTx2Line": trunkRTCNonTimeStampCellsTx2Line,
       "trunkRTCHighPriorityCellsTx2Line": trunkRTCHighPriorityCellsTx2Line,
       "trunkRTCBurstyDataACellsTx2Line": trunkRTCBurstyDataACellsTx2Line,
       "trunkRTCBurstyDataBCellsTx2Line": trunkRTCBurstyDataBCellsTx2Line,
       "trunkRTCTotalCellsTx2Line": trunkRTCTotalCellsTx2Line,
       "trunkRTCTxBurstyDataAClpCellsDropped": trunkRTCTxBurstyDataAClpCellsDropped,
       "trunkRTCTxBurstyDataBClpCellsDropped": trunkRTCTxBurstyDataBClpCellsDropped,
       "trunkRTCBurstyDataAEfcnCellsTx2Line": trunkRTCBurstyDataAEfcnCellsTx2Line,
       "trunkRTCBurstyDataBEfcnCellsTx2Line": trunkRTCBurstyDataBEfcnCellsTx2Line,
       "trunkRTCPlcpOutOfFrames": trunkRTCPlcpOutOfFrames,
       "rtm": rtm,
       "trapsConfig": trapsConfig,
       "trapConfigTable": trapConfigTable,
       "trapConfigEntry": trapConfigEntry,
       "managerIPaddress": managerIPaddress,
       "managerPortNumber": managerPortNumber,
       "managerRowStatus": managerRowStatus,
       "readingTrapFlag": readingTrapFlag,
       "nextTrapSeqNum": nextTrapSeqNum,
       "managerNumOfValidEntries": managerNumOfValidEntries,
       "lastSequenceNumber": lastSequenceNumber,
       "trapUploadTable": trapUploadTable,
       "trapUploadEntry": trapUploadEntry,
       "mgrIpAddress": mgrIpAddress,
       "trapSequenceNum": trapSequenceNum,
       "trapPduString": trapPduString,
       "endOfQueueFlag": endOfQueueFlag,
       "strataviewEvents": strataviewEvents}
)
