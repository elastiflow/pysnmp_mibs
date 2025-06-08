# SNMP MIB module (INFOTEAM-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/infoteam_46086/INFOTEAM-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:49:25 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysDescr,
 sysLocation,
 sysName,
 sysObjectID,
 sysServices,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysDescr",
    "sysLocation",
    "sysName",
    "sysObjectID",
    "sysServices",
    "sysUpTime")

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

infoteam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 46086)
)
if mibBuilder.loadTexts:
    infoteam.setRevisions(
        ("2015-07-30 06:22",
         "2015-06-22 06:41")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class StxRedundancy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRedundancy", 1),
          ("redundancyNok", 2),
          ("redundancyOk", 3))
    )



class StxAdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("standby", 2),
          ("up", 4))
    )



class StxOperStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("downCfg", 1),
          ("standby", 2),
          ("standbyCfg", 3),
          ("up", 4),
          ("upCfg", 5),
          ("unreachable", 6),
          ("noCfg", 7))
    )



class StxProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              10,
              30,
              65,
              75,
              85)
        )
    )
    namedValues = NamedValues(
        *(("dispatch", 1),
          ("manualPoint", 2),
          ("ds", 4),
          ("trigger", 5),
          ("tg", 10),
          ("iec101", 30),
          ("iec61850", 65),
          ("iec104", 75),
          ("snmp", 85))
    )



class StxApplication(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("streamBridge", 1),
          ("streamBrain", 2),
          ("streamWebProxy", 3),
          ("streamLiveData", 4),
          ("streamDataManagement", 5),
          ("streamSynchro", 6),
          ("streamLog", 7),
          ("streamLogReceiver", 8),
          ("streamSystemEvents", 9),
          ("streamDaemon", 10))
    )



# MIB Managed Objects in the order of their OIDs

_IftObjects_ObjectIdentity = ObjectIdentity
iftObjects = _IftObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 1)
)
_IftEvents_ObjectIdentity = ObjectIdentity
iftEvents = _IftEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 2)
)
_IftConf_ObjectIdentity = ObjectIdentity
iftConf = _IftConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 3)
)
_IftGroups_ObjectIdentity = ObjectIdentity
iftGroups = _IftGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 3, 1)
)
_IftCompliances_ObjectIdentity = ObjectIdentity
iftCompliances = _IftCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 3, 2)
)
_IftProducts_ObjectIdentity = ObjectIdentity
iftProducts = _IftProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 4)
)
_IftStreamx_ObjectIdentity = ObjectIdentity
iftStreamx = _IftStreamx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1)
)
_StxSoftware_ObjectIdentity = ObjectIdentity
stxSoftware = _StxSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1)
)
_StxComponents_Object = MibTable
stxComponents = _StxComponents_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stxComponents.setStatus("current")
_StxComponentsEntry_Object = MibTableRow
stxComponentsEntry = _StxComponentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 1, 1)
)
stxComponentsEntry.setIndexNames(
    (0, "INFOTEAM-SNMP-MIB", "stxComponentsIndex"),
)
if mibBuilder.loadTexts:
    stxComponentsEntry.setStatus("current")


class _StxComponentsIndex_Type(Integer32):
    """Custom type stxComponentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StxComponentsIndex_Type.__name__ = "Integer32"
_StxComponentsIndex_Object = MibTableColumn
stxComponentsIndex = _StxComponentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 1, 1, 1),
    _StxComponentsIndex_Type()
)
stxComponentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxComponentsIndex.setStatus("current")
_StxComponentsName_Type = OctetString
_StxComponentsName_Object = MibTableColumn
stxComponentsName = _StxComponentsName_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 1, 1, 2),
    _StxComponentsName_Type()
)
stxComponentsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxComponentsName.setStatus("current")
_StxComponentsInstall_Type = OctetString
_StxComponentsInstall_Object = MibTableColumn
stxComponentsInstall = _StxComponentsInstall_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 1, 1, 3),
    _StxComponentsInstall_Type()
)
stxComponentsInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxComponentsInstall.setStatus("current")
_StxComponentsUpdate_Type = OctetString
_StxComponentsUpdate_Object = MibTableColumn
stxComponentsUpdate = _StxComponentsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 1, 1, 4),
    _StxComponentsUpdate_Type()
)
stxComponentsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxComponentsUpdate.setStatus("current")
_StxComponentsVersion_Type = OctetString
_StxComponentsVersion_Object = MibTableColumn
stxComponentsVersion = _StxComponentsVersion_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 1, 1, 5),
    _StxComponentsVersion_Type()
)
stxComponentsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxComponentsVersion.setStatus("current")
_StxServiceTable_Object = MibTable
stxServiceTable = _StxServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    stxServiceTable.setStatus("current")
_IftServiceEntry_Object = MibTableRow
iftServiceEntry = _IftServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 2, 1)
)
iftServiceEntry.setIndexNames(
    (0, "INFOTEAM-SNMP-MIB", "iftServiceIndex"),
)
if mibBuilder.loadTexts:
    iftServiceEntry.setStatus("current")
_IftServiceIndex_Type = StxApplication
_IftServiceIndex_Object = MibTableColumn
iftServiceIndex = _IftServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 2, 1, 1),
    _IftServiceIndex_Type()
)
iftServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftServiceIndex.setStatus("current")
_IftServiceName_Type = OctetString
_IftServiceName_Object = MibTableColumn
iftServiceName = _IftServiceName_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 2, 1, 2),
    _IftServiceName_Type()
)
iftServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftServiceName.setStatus("current")
_IftServiceDesc_Type = OctetString
_IftServiceDesc_Object = MibTableColumn
iftServiceDesc = _IftServiceDesc_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 2, 1, 3),
    _IftServiceDesc_Type()
)
iftServiceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftServiceDesc.setStatus("current")


class _IftServiceStatus_Type(Integer32):
    """Custom type iftServiceStatus based on Integer32"""
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
        *(("stopped", 1),
          ("startpending", 2),
          ("stoppending", 3),
          ("running", 4),
          ("continuepending", 5),
          ("pausepending", 6),
          ("paused", 7))
    )


_IftServiceStatus_Type.__name__ = "Integer32"
_IftServiceStatus_Object = MibTableColumn
iftServiceStatus = _IftServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 2, 1, 4),
    _IftServiceStatus_Type()
)
iftServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftServiceStatus.setStatus("current")
_IftServiceCpuUsage_Type = Integer32
_IftServiceCpuUsage_Object = MibTableColumn
iftServiceCpuUsage = _IftServiceCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 2, 1, 5),
    _IftServiceCpuUsage_Type()
)
iftServiceCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftServiceCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    iftServiceCpuUsage.setUnits("%")
_IftServiceMemoryUsage_Type = Integer32
_IftServiceMemoryUsage_Object = MibTableColumn
iftServiceMemoryUsage = _IftServiceMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 2, 1, 6),
    _IftServiceMemoryUsage_Type()
)
iftServiceMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftServiceMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    iftServiceMemoryUsage.setUnits("%")
_IftServiceMemoryUsed_Type = Integer32
_IftServiceMemoryUsed_Object = MibTableColumn
iftServiceMemoryUsed = _IftServiceMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 2, 1, 7),
    _IftServiceMemoryUsed_Type()
)
iftServiceMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftServiceMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    iftServiceMemoryUsed.setUnits("MB")
_StxSetupVersion_Type = OctetString
_StxSetupVersion_Object = MibScalar
stxSetupVersion = _StxSetupVersion_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 3),
    _StxSetupVersion_Type()
)
stxSetupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxSetupVersion.setStatus("current")
_StxStreamXVersion_Type = OctetString
_StxStreamXVersion_Object = MibScalar
stxStreamXVersion = _StxStreamXVersion_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 4),
    _StxStreamXVersion_Type()
)
stxStreamXVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxStreamXVersion.setStatus("current")
_StxFirstInstall_Type = OctetString
_StxFirstInstall_Object = MibScalar
stxFirstInstall = _StxFirstInstall_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 5),
    _StxFirstInstall_Type()
)
stxFirstInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxFirstInstall.setStatus("current")
_StxLastInstall_Type = OctetString
_StxLastInstall_Object = MibScalar
stxLastInstall = _StxLastInstall_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 1, 6),
    _StxLastInstall_Type()
)
stxLastInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxLastInstall.setStatus("current")
_StxHardware_ObjectIdentity = ObjectIdentity
stxHardware = _StxHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2)
)
_StxNetworkInterfaceTable_Object = MibTable
stxNetworkInterfaceTable = _StxNetworkInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    stxNetworkInterfaceTable.setStatus("current")
_StxNetworkInterfaceEntry_Object = MibTableRow
stxNetworkInterfaceEntry = _StxNetworkInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 1, 1)
)
stxNetworkInterfaceEntry.setIndexNames(
    (0, "INFOTEAM-SNMP-MIB", "iftNetIfIndex"),
)
if mibBuilder.loadTexts:
    stxNetworkInterfaceEntry.setStatus("current")


class _IftNetIfIndex_Type(Integer32):
    """Custom type iftNetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IftNetIfIndex_Type.__name__ = "Integer32"
_IftNetIfIndex_Object = MibTableColumn
iftNetIfIndex = _IftNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 1, 1, 1),
    _IftNetIfIndex_Type()
)
iftNetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftNetIfIndex.setStatus("current")
_IftNetIfName_Type = OctetString
_IftNetIfName_Object = MibTableColumn
iftNetIfName = _IftNetIfName_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 1, 1, 2),
    _IftNetIfName_Type()
)
iftNetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftNetIfName.setStatus("current")


class _IftNetIfOperStatus_Type(Integer32):
    """Custom type iftNetIfOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_IftNetIfOperStatus_Type.__name__ = "Integer32"
_IftNetIfOperStatus_Object = MibTableColumn
iftNetIfOperStatus = _IftNetIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 1, 1, 3),
    _IftNetIfOperStatus_Type()
)
iftNetIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftNetIfOperStatus.setStatus("current")
_StxCpuTable_Object = MibTable
stxCpuTable = _StxCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    stxCpuTable.setStatus("current")
_StxCpuEntry_Object = MibTableRow
stxCpuEntry = _StxCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 2, 1)
)
stxCpuEntry.setIndexNames(
    (0, "INFOTEAM-SNMP-MIB", "stxCpuIndex"),
)
if mibBuilder.loadTexts:
    stxCpuEntry.setStatus("current")


class _StxCpuIndex_Type(Integer32):
    """Custom type stxCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_StxCpuIndex_Type.__name__ = "Integer32"
_StxCpuIndex_Object = MibTableColumn
stxCpuIndex = _StxCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 2, 1, 1),
    _StxCpuIndex_Type()
)
stxCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxCpuIndex.setStatus("current")
_StxCpuUsage_Type = Integer32
_StxCpuUsage_Object = MibTableColumn
stxCpuUsage = _StxCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 2, 1, 2),
    _StxCpuUsage_Type()
)
stxCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    stxCpuUsage.setUnits("%")
_StxPowerSupplyTable_Object = MibTable
stxPowerSupplyTable = _StxPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    stxPowerSupplyTable.setStatus("current")
_StxPowerSupplyEntry_Object = MibTableRow
stxPowerSupplyEntry = _StxPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 3, 1)
)
stxPowerSupplyEntry.setIndexNames(
    (0, "INFOTEAM-SNMP-MIB", "iftPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    stxPowerSupplyEntry.setStatus("current")


class _IftPowerSupplyIndex_Type(Integer32):
    """Custom type iftPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_IftPowerSupplyIndex_Type.__name__ = "Integer32"
_IftPowerSupplyIndex_Object = MibTableColumn
iftPowerSupplyIndex = _IftPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 3, 1, 1),
    _IftPowerSupplyIndex_Type()
)
iftPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftPowerSupplyIndex.setStatus("current")


class _IftPowerSupplyStatus_Type(Integer32):
    """Custom type iftPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nok", 0),
          ("ok", 1))
    )


_IftPowerSupplyStatus_Type.__name__ = "Integer32"
_IftPowerSupplyStatus_Object = MibTableColumn
iftPowerSupplyStatus = _IftPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 3, 1, 3),
    _IftPowerSupplyStatus_Type()
)
iftPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iftPowerSupplyStatus.setStatus("current")
_StxHarddiskTable_Object = MibTable
stxHarddiskTable = _StxHarddiskTable_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    stxHarddiskTable.setStatus("current")
_StxHarddiskEntry_Object = MibTableRow
stxHarddiskEntry = _StxHarddiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 4, 1)
)
stxHarddiskEntry.setIndexNames(
    (0, "INFOTEAM-SNMP-MIB", "stxHarddiskIndex"),
)
if mibBuilder.loadTexts:
    stxHarddiskEntry.setStatus("current")


class _StxHarddiskIndex_Type(Integer32):
    """Custom type stxHarddiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StxHarddiskIndex_Type.__name__ = "Integer32"
_StxHarddiskIndex_Object = MibTableColumn
stxHarddiskIndex = _StxHarddiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 4, 1, 1),
    _StxHarddiskIndex_Type()
)
stxHarddiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxHarddiskIndex.setStatus("current")
_StxHarddiskName_Type = OctetString
_StxHarddiskName_Object = MibTableColumn
stxHarddiskName = _StxHarddiskName_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 4, 1, 2),
    _StxHarddiskName_Type()
)
stxHarddiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxHarddiskName.setStatus("current")
_StxHarddiskFreeSpace_Type = Integer32
_StxHarddiskFreeSpace_Object = MibTableColumn
stxHarddiskFreeSpace = _StxHarddiskFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 4, 1, 3),
    _StxHarddiskFreeSpace_Type()
)
stxHarddiskFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxHarddiskFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    stxHarddiskFreeSpace.setUnits("MB")
_StxHarddiskUsedSpace_Type = Integer32
_StxHarddiskUsedSpace_Object = MibTableColumn
stxHarddiskUsedSpace = _StxHarddiskUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 4, 1, 4),
    _StxHarddiskUsedSpace_Type()
)
stxHarddiskUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxHarddiskUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    stxHarddiskUsedSpace.setUnits("%")
_StxHarddiskTotalSpace_Type = Integer32
_StxHarddiskTotalSpace_Object = MibTableColumn
stxHarddiskTotalSpace = _StxHarddiskTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 4, 1, 5),
    _StxHarddiskTotalSpace_Type()
)
stxHarddiskTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxHarddiskTotalSpace.setStatus("current")
if mibBuilder.loadTexts:
    stxHarddiskTotalSpace.setUnits("MB")
_StxHarddiskUsage_Type = Integer32
_StxHarddiskUsage_Object = MibTableColumn
stxHarddiskUsage = _StxHarddiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 4, 1, 6),
    _StxHarddiskUsage_Type()
)
stxHarddiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxHarddiskUsage.setStatus("current")
if mibBuilder.loadTexts:
    stxHarddiskUsage.setUnits("%")
_StxHarddiskType_Type = Integer32
_StxHarddiskType_Object = MibTableColumn
stxHarddiskType = _StxHarddiskType_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 4, 1, 7),
    _StxHarddiskType_Type()
)
stxHarddiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxHarddiskType.setStatus("current")
_StxTotalMemory_Type = Integer32
_StxTotalMemory_Object = MibScalar
stxTotalMemory = _StxTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 6),
    _StxTotalMemory_Type()
)
stxTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxTotalMemory.setStatus("current")
if mibBuilder.loadTexts:
    stxTotalMemory.setUnits("MB")
_StxHardwareWarning_Type = Integer32
_StxHardwareWarning_Object = MibScalar
stxHardwareWarning = _StxHardwareWarning_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 7),
    _StxHardwareWarning_Type()
)
stxHardwareWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxHardwareWarning.setStatus("current")
_StxHardwareFailure_Type = Integer32
_StxHardwareFailure_Object = MibScalar
stxHardwareFailure = _StxHardwareFailure_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 8),
    _StxHardwareFailure_Type()
)
stxHardwareFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxHardwareFailure.setStatus("current")
_StxMemoryUsage_Type = Integer32
_StxMemoryUsage_Object = MibScalar
stxMemoryUsage = _StxMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 9),
    _StxMemoryUsage_Type()
)
stxMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    stxMemoryUsage.setUnits("%")
_StxMemoryUsed_Type = Integer32
_StxMemoryUsed_Object = MibScalar
stxMemoryUsed = _StxMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 10),
    _StxMemoryUsed_Type()
)
stxMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    stxMemoryUsed.setUnits("MB")
_StxTotalCpuUsage_Type = Integer32
_StxTotalCpuUsage_Object = MibScalar
stxTotalCpuUsage = _StxTotalCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 2, 11),
    _StxTotalCpuUsage_Type()
)
stxTotalCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxTotalCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    stxTotalCpuUsage.setUnits("%")
_StxProcess_ObjectIdentity = ObjectIdentity
stxProcess = _StxProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3)
)
_StxStreamBridgeTable_Object = MibTable
stxStreamBridgeTable = _StxStreamBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    stxStreamBridgeTable.setStatus("current")
_StxStreamBridgeEntry_Object = MibTableRow
stxStreamBridgeEntry = _StxStreamBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 1, 1)
)
stxStreamBridgeEntry.setIndexNames(
    (0, "INFOTEAM-SNMP-MIB", "stxStreamBridgeIndex"),
)
if mibBuilder.loadTexts:
    stxStreamBridgeEntry.setStatus("current")


class _StxStreamBridgeIndex_Type(Integer32):
    """Custom type stxStreamBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_StxStreamBridgeIndex_Type.__name__ = "Integer32"
_StxStreamBridgeIndex_Object = MibTableColumn
stxStreamBridgeIndex = _StxStreamBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 1, 1, 1),
    _StxStreamBridgeIndex_Type()
)
stxStreamBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxStreamBridgeIndex.setStatus("current")
_StxStreamBridgeHost_Type = OctetString
_StxStreamBridgeHost_Object = MibTableColumn
stxStreamBridgeHost = _StxStreamBridgeHost_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 1, 1, 2),
    _StxStreamBridgeHost_Type()
)
stxStreamBridgeHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxStreamBridgeHost.setStatus("current")
_StxStreamBridgeOperStatus_Type = StxOperStatus
_StxStreamBridgeOperStatus_Object = MibTableColumn
stxStreamBridgeOperStatus = _StxStreamBridgeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 1, 1, 3),
    _StxStreamBridgeOperStatus_Type()
)
stxStreamBridgeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxStreamBridgeOperStatus.setStatus("current")
_StxStreamBridgeAdminStatus_Type = StxAdminStatus
_StxStreamBridgeAdminStatus_Object = MibTableColumn
stxStreamBridgeAdminStatus = _StxStreamBridgeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 1, 1, 4),
    _StxStreamBridgeAdminStatus_Type()
)
stxStreamBridgeAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxStreamBridgeAdminStatus.setStatus("current")
_StxStreamBridgeRedundancyStatus_Type = StxRedundancy
_StxStreamBridgeRedundancyStatus_Object = MibTableColumn
stxStreamBridgeRedundancyStatus = _StxStreamBridgeRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 1, 1, 5),
    _StxStreamBridgeRedundancyStatus_Type()
)
stxStreamBridgeRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxStreamBridgeRedundancyStatus.setStatus("current")
_StxStreamBridgeEntryRedundancyError_Type = Integer32
_StxStreamBridgeEntryRedundancyError_Object = MibTableColumn
stxStreamBridgeEntryRedundancyError = _StxStreamBridgeEntryRedundancyError_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 1, 1, 6),
    _StxStreamBridgeEntryRedundancyError_Type()
)
stxStreamBridgeEntryRedundancyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxStreamBridgeEntryRedundancyError.setStatus("current")
_StxStreamBridgeEntryUsrLogged_Type = Integer32
_StxStreamBridgeEntryUsrLogged_Object = MibTableColumn
stxStreamBridgeEntryUsrLogged = _StxStreamBridgeEntryUsrLogged_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 1, 1, 7),
    _StxStreamBridgeEntryUsrLogged_Type()
)
stxStreamBridgeEntryUsrLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxStreamBridgeEntryUsrLogged.setStatus("current")
_StxModuleTable_Object = MibTable
stxModuleTable = _StxModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    stxModuleTable.setStatus("current")
_StxModuleEntry_Object = MibTableRow
stxModuleEntry = _StxModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 2, 1)
)
stxModuleEntry.setIndexNames(
    (0, "INFOTEAM-SNMP-MIB", "stxModuleType"),
)
if mibBuilder.loadTexts:
    stxModuleEntry.setStatus("current")
_StxModuleType_Type = StxProtocol
_StxModuleType_Object = MibTableColumn
stxModuleType = _StxModuleType_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 2, 1, 1),
    _StxModuleType_Type()
)
stxModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxModuleType.setStatus("current")
_StxModuleOpcName_Type = OctetString
_StxModuleOpcName_Object = MibTableColumn
stxModuleOpcName = _StxModuleOpcName_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 2, 1, 2),
    _StxModuleOpcName_Type()
)
stxModuleOpcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxModuleOpcName.setStatus("current")


class _StxModuleCode_Type(Integer32):
    """Custom type stxModuleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483648),
    )


_StxModuleCode_Type.__name__ = "Integer32"
_StxModuleCode_Object = MibTableColumn
stxModuleCode = _StxModuleCode_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 2, 1, 3),
    _StxModuleCode_Type()
)
stxModuleCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxModuleCode.setStatus("current")
_StxModuleAdminStatus_Type = StxAdminStatus
_StxModuleAdminStatus_Object = MibTableColumn
stxModuleAdminStatus = _StxModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 2, 1, 4),
    _StxModuleAdminStatus_Type()
)
stxModuleAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxModuleAdminStatus.setStatus("current")
_StxModuleOperStatus_Type = StxOperStatus
_StxModuleOperStatus_Object = MibTableColumn
stxModuleOperStatus = _StxModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 2, 1, 5),
    _StxModuleOperStatus_Type()
)
stxModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxModuleOperStatus.setStatus("current")
_StxObjectTable_Object = MibTable
stxObjectTable = _StxObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    stxObjectTable.setStatus("current")
_StxObjectEntry_Object = MibTableRow
stxObjectEntry = _StxObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 3, 1)
)
stxObjectEntry.setIndexNames(
    (0, "INFOTEAM-SNMP-MIB", "stxObjectCode"),
)
if mibBuilder.loadTexts:
    stxObjectEntry.setStatus("current")


class _StxObjectCode_Type(Integer32):
    """Custom type stxObjectCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483648),
    )


_StxObjectCode_Type.__name__ = "Integer32"
_StxObjectCode_Object = MibTableColumn
stxObjectCode = _StxObjectCode_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 3, 1, 1),
    _StxObjectCode_Type()
)
stxObjectCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxObjectCode.setStatus("current")
_StxObjectName_Type = OctetString
_StxObjectName_Object = MibTableColumn
stxObjectName = _StxObjectName_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 3, 1, 2),
    _StxObjectName_Type()
)
stxObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxObjectName.setStatus("current")
_StxObjectValue_Type = OctetString
_StxObjectValue_Object = MibTableColumn
stxObjectValue = _StxObjectValue_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 3, 1, 3),
    _StxObjectValue_Type()
)
stxObjectValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxObjectValue.setStatus("current")


class _StxObjectQuality_Type(Integer32):
    """Custom type stxObjectQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              8,
              20,
              28,
              64,
              192,
              216)
        )
    )
    namedValues = NamedValues(
        *(("null", -1),
          ("bad", 0),
          ("notConnected", 8),
          ("lastKnown", 20),
          ("outOfService", 28),
          ("uncertain", 64),
          ("good", 192),
          ("localOverride", 216))
    )


_StxObjectQuality_Type.__name__ = "Integer32"
_StxObjectQuality_Object = MibTableColumn
stxObjectQuality = _StxObjectQuality_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 3, 1, 4),
    _StxObjectQuality_Type()
)
stxObjectQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxObjectQuality.setStatus("current")
_StxObjectTimestamp_Type = OctetString
_StxObjectTimestamp_Object = MibTableColumn
stxObjectTimestamp = _StxObjectTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 3, 3, 1, 5),
    _StxObjectTimestamp_Type()
)
stxObjectTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stxObjectTimestamp.setStatus("current")
_StxTraps_ObjectIdentity = ObjectIdentity
stxTraps = _StxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 4)
)

# Managed Objects groups

iftBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46086, 3, 1, 1)
)
iftBasicGroup.setObjects(
      *(("INFOTEAM-SNMP-MIB", "stxComponentsIndex"),
        ("INFOTEAM-SNMP-MIB", "stxComponentsName"),
        ("INFOTEAM-SNMP-MIB", "stxComponentsInstall"),
        ("INFOTEAM-SNMP-MIB", "stxComponentsUpdate"),
        ("INFOTEAM-SNMP-MIB", "stxComponentsVersion"),
        ("INFOTEAM-SNMP-MIB", "iftServiceIndex"),
        ("INFOTEAM-SNMP-MIB", "iftServiceName"),
        ("INFOTEAM-SNMP-MIB", "iftServiceDesc"),
        ("INFOTEAM-SNMP-MIB", "iftServiceStatus"),
        ("INFOTEAM-SNMP-MIB", "iftServiceCpuUsage"),
        ("INFOTEAM-SNMP-MIB", "iftServiceMemoryUsage"),
        ("INFOTEAM-SNMP-MIB", "iftServiceMemoryUsed"),
        ("INFOTEAM-SNMP-MIB", "stxSetupVersion"),
        ("INFOTEAM-SNMP-MIB", "stxStreamXVersion"),
        ("INFOTEAM-SNMP-MIB", "stxFirstInstall"),
        ("INFOTEAM-SNMP-MIB", "stxLastInstall"),
        ("INFOTEAM-SNMP-MIB", "iftNetIfIndex"),
        ("INFOTEAM-SNMP-MIB", "iftNetIfName"),
        ("INFOTEAM-SNMP-MIB", "iftNetIfOperStatus"),
        ("INFOTEAM-SNMP-MIB", "stxCpuIndex"),
        ("INFOTEAM-SNMP-MIB", "stxCpuUsage"),
        ("INFOTEAM-SNMP-MIB", "iftPowerSupplyIndex"),
        ("INFOTEAM-SNMP-MIB", "iftPowerSupplyStatus"),
        ("INFOTEAM-SNMP-MIB", "stxHarddiskIndex"),
        ("INFOTEAM-SNMP-MIB", "stxHarddiskName"),
        ("INFOTEAM-SNMP-MIB", "stxHarddiskFreeSpace"),
        ("INFOTEAM-SNMP-MIB", "stxHarddiskUsedSpace"),
        ("INFOTEAM-SNMP-MIB", "stxHarddiskTotalSpace"),
        ("INFOTEAM-SNMP-MIB", "stxHarddiskUsage"),
        ("INFOTEAM-SNMP-MIB", "stxHarddiskType"),
        ("INFOTEAM-SNMP-MIB", "stxTotalMemory"),
        ("INFOTEAM-SNMP-MIB", "stxHardwareWarning"),
        ("INFOTEAM-SNMP-MIB", "stxHardwareFailure"),
        ("INFOTEAM-SNMP-MIB", "stxMemoryUsage"),
        ("INFOTEAM-SNMP-MIB", "stxMemoryUsed"),
        ("INFOTEAM-SNMP-MIB", "stxTotalCpuUsage"),
        ("INFOTEAM-SNMP-MIB", "stxStreamBridgeIndex"),
        ("INFOTEAM-SNMP-MIB", "stxStreamBridgeHost"),
        ("INFOTEAM-SNMP-MIB", "stxStreamBridgeOperStatus"),
        ("INFOTEAM-SNMP-MIB", "stxStreamBridgeAdminStatus"),
        ("INFOTEAM-SNMP-MIB", "stxStreamBridgeRedundancyStatus"),
        ("INFOTEAM-SNMP-MIB", "stxStreamBridgeEntryRedundancyError"),
        ("INFOTEAM-SNMP-MIB", "stxStreamBridgeEntryUsrLogged"),
        ("INFOTEAM-SNMP-MIB", "stxModuleType"),
        ("INFOTEAM-SNMP-MIB", "stxModuleOpcName"),
        ("INFOTEAM-SNMP-MIB", "stxModuleCode"),
        ("INFOTEAM-SNMP-MIB", "stxModuleAdminStatus"),
        ("INFOTEAM-SNMP-MIB", "stxModuleOperStatus"),
        ("INFOTEAM-SNMP-MIB", "stxObjectCode"),
        ("INFOTEAM-SNMP-MIB", "stxObjectName"),
        ("INFOTEAM-SNMP-MIB", "stxObjectValue"),
        ("INFOTEAM-SNMP-MIB", "stxObjectQuality"),
        ("INFOTEAM-SNMP-MIB", "stxObjectTimestamp"))
)
if mibBuilder.loadTexts:
    iftBasicGroup.setStatus("current")


# Notification objects

stxLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 4, 1)
)
stxLinkDown.setObjects(
      *(("INFOTEAM-SNMP-MIB", "iftNetIfIndex"),
        ("INFOTEAM-SNMP-MIB", "iftNetIfName"),
        ("INFOTEAM-SNMP-MIB", "iftNetIfOperStatus"))
)
if mibBuilder.loadTexts:
    stxLinkDown.setStatus(
        "current"
    )

stxLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 4, 2)
)
stxLinkUp.setObjects(
      *(("INFOTEAM-SNMP-MIB", "iftNetIfIndex"),
        ("INFOTEAM-SNMP-MIB", "iftNetIfName"),
        ("INFOTEAM-SNMP-MIB", "iftNetIfOperStatus"))
)
if mibBuilder.loadTexts:
    stxLinkUp.setStatus(
        "current"
    )

stxPowerSupplyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 4, 3)
)
stxPowerSupplyDown.setObjects(
      *(("INFOTEAM-SNMP-MIB", "iftPowerSupplyIndex"),
        ("INFOTEAM-SNMP-MIB", "iftPowerSupplyStatus"))
)
if mibBuilder.loadTexts:
    stxPowerSupplyDown.setStatus(
        "current"
    )

stxPowerSupplyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 46086, 4, 1, 4, 4)
)
stxPowerSupplyUp.setObjects(
      *(("INFOTEAM-SNMP-MIB", "iftPowerSupplyIndex"),
        ("INFOTEAM-SNMP-MIB", "iftPowerSupplyStatus"))
)
if mibBuilder.loadTexts:
    stxPowerSupplyUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFOTEAM-SNMP-MIB",
    **{"StxRedundancy": StxRedundancy,
       "StxAdminStatus": StxAdminStatus,
       "StxOperStatus": StxOperStatus,
       "StxProtocol": StxProtocol,
       "StxApplication": StxApplication,
       "infoteam": infoteam,
       "iftObjects": iftObjects,
       "iftEvents": iftEvents,
       "iftConf": iftConf,
       "iftGroups": iftGroups,
       "iftBasicGroup": iftBasicGroup,
       "iftCompliances": iftCompliances,
       "iftProducts": iftProducts,
       "iftStreamx": iftStreamx,
       "stxSoftware": stxSoftware,
       "stxComponents": stxComponents,
       "stxComponentsEntry": stxComponentsEntry,
       "stxComponentsIndex": stxComponentsIndex,
       "stxComponentsName": stxComponentsName,
       "stxComponentsInstall": stxComponentsInstall,
       "stxComponentsUpdate": stxComponentsUpdate,
       "stxComponentsVersion": stxComponentsVersion,
       "stxServiceTable": stxServiceTable,
       "iftServiceEntry": iftServiceEntry,
       "iftServiceIndex": iftServiceIndex,
       "iftServiceName": iftServiceName,
       "iftServiceDesc": iftServiceDesc,
       "iftServiceStatus": iftServiceStatus,
       "iftServiceCpuUsage": iftServiceCpuUsage,
       "iftServiceMemoryUsage": iftServiceMemoryUsage,
       "iftServiceMemoryUsed": iftServiceMemoryUsed,
       "stxSetupVersion": stxSetupVersion,
       "stxStreamXVersion": stxStreamXVersion,
       "stxFirstInstall": stxFirstInstall,
       "stxLastInstall": stxLastInstall,
       "stxHardware": stxHardware,
       "stxNetworkInterfaceTable": stxNetworkInterfaceTable,
       "stxNetworkInterfaceEntry": stxNetworkInterfaceEntry,
       "iftNetIfIndex": iftNetIfIndex,
       "iftNetIfName": iftNetIfName,
       "iftNetIfOperStatus": iftNetIfOperStatus,
       "stxCpuTable": stxCpuTable,
       "stxCpuEntry": stxCpuEntry,
       "stxCpuIndex": stxCpuIndex,
       "stxCpuUsage": stxCpuUsage,
       "stxPowerSupplyTable": stxPowerSupplyTable,
       "stxPowerSupplyEntry": stxPowerSupplyEntry,
       "iftPowerSupplyIndex": iftPowerSupplyIndex,
       "iftPowerSupplyStatus": iftPowerSupplyStatus,
       "stxHarddiskTable": stxHarddiskTable,
       "stxHarddiskEntry": stxHarddiskEntry,
       "stxHarddiskIndex": stxHarddiskIndex,
       "stxHarddiskName": stxHarddiskName,
       "stxHarddiskFreeSpace": stxHarddiskFreeSpace,
       "stxHarddiskUsedSpace": stxHarddiskUsedSpace,
       "stxHarddiskTotalSpace": stxHarddiskTotalSpace,
       "stxHarddiskUsage": stxHarddiskUsage,
       "stxHarddiskType": stxHarddiskType,
       "stxTotalMemory": stxTotalMemory,
       "stxHardwareWarning": stxHardwareWarning,
       "stxHardwareFailure": stxHardwareFailure,
       "stxMemoryUsage": stxMemoryUsage,
       "stxMemoryUsed": stxMemoryUsed,
       "stxTotalCpuUsage": stxTotalCpuUsage,
       "stxProcess": stxProcess,
       "stxStreamBridgeTable": stxStreamBridgeTable,
       "stxStreamBridgeEntry": stxStreamBridgeEntry,
       "stxStreamBridgeIndex": stxStreamBridgeIndex,
       "stxStreamBridgeHost": stxStreamBridgeHost,
       "stxStreamBridgeOperStatus": stxStreamBridgeOperStatus,
       "stxStreamBridgeAdminStatus": stxStreamBridgeAdminStatus,
       "stxStreamBridgeRedundancyStatus": stxStreamBridgeRedundancyStatus,
       "stxStreamBridgeEntryRedundancyError": stxStreamBridgeEntryRedundancyError,
       "stxStreamBridgeEntryUsrLogged": stxStreamBridgeEntryUsrLogged,
       "stxModuleTable": stxModuleTable,
       "stxModuleEntry": stxModuleEntry,
       "stxModuleType": stxModuleType,
       "stxModuleOpcName": stxModuleOpcName,
       "stxModuleCode": stxModuleCode,
       "stxModuleAdminStatus": stxModuleAdminStatus,
       "stxModuleOperStatus": stxModuleOperStatus,
       "stxObjectTable": stxObjectTable,
       "stxObjectEntry": stxObjectEntry,
       "stxObjectCode": stxObjectCode,
       "stxObjectName": stxObjectName,
       "stxObjectValue": stxObjectValue,
       "stxObjectQuality": stxObjectQuality,
       "stxObjectTimestamp": stxObjectTimestamp,
       "stxTraps": stxTraps,
       "stxLinkDown": stxLinkDown,
       "stxLinkUp": stxLinkUp,
       "stxPowerSupplyDown": stxPowerSupplyDown,
       "stxPowerSupplyUp": stxPowerSupplyUp}
)
