# SNMP MIB module (TN-RMD-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-RMD-SYSTEM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:06:36 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "VlanId")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(TnRmdAccessIfIndex,
 TnRmdItemCode,
 TnRmdOui,
 TnRmdPcp,
 TnRmdTpid,
 TnRmdVersion) = mibBuilder.importSymbols(
    "TN-RMD-TC-MIB",
    "TnRmdAccessIfIndex",
    "TnRmdItemCode",
    "TnRmdOui",
    "TnRmdPcp",
    "TnRmdTpid",
    "TnRmdVersion")

(TItemDescription,
 TmnxEncapVal,
 TmnxPortID) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TItemDescription",
    "TmnxEncapVal",
    "TmnxPortID")

(tnRmdMIBModules,
 tnRmdObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnRmdMIBModules",
    "tnRmdObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnRmdSystemMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 4, 4)
)
if mibBuilder.loadTexts:
    tnRmdSystemMibModule.setRevisions(
        ("2012-11-28 00:00",
         "2013-08-09 00:00",
         "2014-04-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnRmdDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254)
        )
    )
    namedValues = NamedValues(
        *(("efm", 0),
          ("cfm", 1),
          ("cedd", 2),
          ("tsopOC3", 3),
          ("tsopOC12", 4),
          ("unknown", 254))
    )



class TnRmdDiscoveryMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pollAll", 0),
          ("pollGroup", 1))
    )



class TnRmdNumberOfVlanTags(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )



class TnRmdSwImageState(TextualConvention, Integer32):
    status = "current"
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
        *(("swImageActive", 1),
          ("swImageInactive", 2),
          ("swImageEmpty", 3),
          ("swImageError", 4),
          ("swImageSoak", 5))
    )



class TnRmdSystemId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class TnRmdSystemLocation(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32



class TnRmdSystemManagementMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("mgmtModeIntegrated", 0),
          ("mgmtModeStandalone", 1),
          ("mgmtModeNotApplicable", 255))
    )



class TnRmdSystemName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32



class TnRmdSystemResetType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("resetWarm1", 0),
          ("resetWarm2", 1),
          ("resetWarm3", 2),
          ("resetCold", 3),
          ("noCmd", 255))
    )



class TnRmdSystemDeviceStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("normal", 1),
          ("ndf", 2),
          ("dnr", 3),
          ("wdp", 4),
          ("pwr", 5),
          ("eqf", 6))
    )



class TnRmdSystemRmdAccessIfType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("sap", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnRmdSystemObjects_ObjectIdentity = ObjectIdentity
tnRmdSystemObjects = _TnRmdSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4)
)
_TnRmdSystemAttributeTotal_Type = Integer32
_TnRmdSystemAttributeTotal_Object = MibScalar
tnRmdSystemAttributeTotal = _TnRmdSystemAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 1),
    _TnRmdSystemAttributeTotal_Type()
)
tnRmdSystemAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemAttributeTotal.setStatus("current")
_TnRmdDiscoverySystemTable_Object = MibTable
tnRmdDiscoverySystemTable = _TnRmdDiscoverySystemTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tnRmdDiscoverySystemTable.setStatus("current")
_TnRmdDiscoverySystemEntry_Object = MibTableRow
tnRmdDiscoverySystemEntry = _TnRmdDiscoverySystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1)
)
tnRmdDiscoverySystemEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnRmdDiscoverySystemEntry.setStatus("current")
_TnRmdDiscoveryMcMacAddress_Type = MacAddress
_TnRmdDiscoveryMcMacAddress_Object = MibTableColumn
tnRmdDiscoveryMcMacAddress = _TnRmdDiscoveryMcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 1),
    _TnRmdDiscoveryMcMacAddress_Type()
)
tnRmdDiscoveryMcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryMcMacAddress.setStatus("current")
_TnRmdDiscoveryMode_Type = TnRmdDiscoveryMode
_TnRmdDiscoveryMode_Object = MibTableColumn
tnRmdDiscoveryMode = _TnRmdDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 2),
    _TnRmdDiscoveryMode_Type()
)
tnRmdDiscoveryMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryMode.setStatus("current")
_TnRmdDiscoveryNumberOfVlanTags_Type = TnRmdNumberOfVlanTags
_TnRmdDiscoveryNumberOfVlanTags_Object = MibTableColumn
tnRmdDiscoveryNumberOfVlanTags = _TnRmdDiscoveryNumberOfVlanTags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 3),
    _TnRmdDiscoveryNumberOfVlanTags_Type()
)
tnRmdDiscoveryNumberOfVlanTags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryNumberOfVlanTags.setStatus("current")
_TnRmdDiscoveryOuterTPID_Type = TnRmdTpid
_TnRmdDiscoveryOuterTPID_Object = MibTableColumn
tnRmdDiscoveryOuterTPID = _TnRmdDiscoveryOuterTPID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 4),
    _TnRmdDiscoveryOuterTPID_Type()
)
tnRmdDiscoveryOuterTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryOuterTPID.setStatus("current")
_TnRmdDiscoveryOuterVlanId_Type = VlanId
_TnRmdDiscoveryOuterVlanId_Object = MibTableColumn
tnRmdDiscoveryOuterVlanId = _TnRmdDiscoveryOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 5),
    _TnRmdDiscoveryOuterVlanId_Type()
)
tnRmdDiscoveryOuterVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryOuterVlanId.setStatus("current")
_TnRmdDiscoveryOuterPCP_Type = TnRmdPcp
_TnRmdDiscoveryOuterPCP_Object = MibTableColumn
tnRmdDiscoveryOuterPCP = _TnRmdDiscoveryOuterPCP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 6),
    _TnRmdDiscoveryOuterPCP_Type()
)
tnRmdDiscoveryOuterPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryOuterPCP.setStatus("current")
_TnRmdDiscoveryOuterDEI_Type = TruthValue
_TnRmdDiscoveryOuterDEI_Object = MibTableColumn
tnRmdDiscoveryOuterDEI = _TnRmdDiscoveryOuterDEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 7),
    _TnRmdDiscoveryOuterDEI_Type()
)
tnRmdDiscoveryOuterDEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryOuterDEI.setStatus("current")
_TnRmdDiscoveryInnerTPID_Type = TnRmdTpid
_TnRmdDiscoveryInnerTPID_Object = MibTableColumn
tnRmdDiscoveryInnerTPID = _TnRmdDiscoveryInnerTPID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 8),
    _TnRmdDiscoveryInnerTPID_Type()
)
tnRmdDiscoveryInnerTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryInnerTPID.setStatus("current")
_TnRmdDiscoveryInnerVlanId_Type = VlanId
_TnRmdDiscoveryInnerVlanId_Object = MibTableColumn
tnRmdDiscoveryInnerVlanId = _TnRmdDiscoveryInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 9),
    _TnRmdDiscoveryInnerVlanId_Type()
)
tnRmdDiscoveryInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryInnerVlanId.setStatus("current")
_TnRmdDiscoveryInnerPCP_Type = TnRmdPcp
_TnRmdDiscoveryInnerPCP_Object = MibTableColumn
tnRmdDiscoveryInnerPCP = _TnRmdDiscoveryInnerPCP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 10),
    _TnRmdDiscoveryInnerPCP_Type()
)
tnRmdDiscoveryInnerPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryInnerPCP.setStatus("current")
_TnRmdDiscoveryInnerDEI_Type = TruthValue
_TnRmdDiscoveryInnerDEI_Object = MibTableColumn
tnRmdDiscoveryInnerDEI = _TnRmdDiscoveryInnerDEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 11),
    _TnRmdDiscoveryInnerDEI_Type()
)
tnRmdDiscoveryInnerDEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryInnerDEI.setStatus("current")
_TnRmdDiscoveryRmdAccessIf_Type = TnRmdAccessIfIndex
_TnRmdDiscoveryRmdAccessIf_Object = MibTableColumn
tnRmdDiscoveryRmdAccessIf = _TnRmdDiscoveryRmdAccessIf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 12),
    _TnRmdDiscoveryRmdAccessIf_Type()
)
tnRmdDiscoveryRmdAccessIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryRmdAccessIf.setStatus("current")
_TnRmdDiscoveryOui_Type = TnRmdOui
_TnRmdDiscoveryOui_Object = MibTableColumn
tnRmdDiscoveryOui = _TnRmdDiscoveryOui_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 2, 1, 13),
    _TnRmdDiscoveryOui_Type()
)
tnRmdDiscoveryOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryOui.setStatus("current")
_TnRmdDiscoverySystemStartTable_Object = MibTable
tnRmdDiscoverySystemStartTable = _TnRmdDiscoverySystemStartTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tnRmdDiscoverySystemStartTable.setStatus("current")
_TnRmdDiscoverySystemStartEntry_Object = MibTableRow
tnRmdDiscoverySystemStartEntry = _TnRmdDiscoverySystemStartEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 3, 1)
)
tnRmdDiscoverySystemStartEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnRmdDiscoverySystemStartEntry.setStatus("current")
_TnRmdDiscoveryStart_Type = TruthValue
_TnRmdDiscoveryStart_Object = MibTableColumn
tnRmdDiscoveryStart = _TnRmdDiscoveryStart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 3, 1, 1),
    _TnRmdDiscoveryStart_Type()
)
tnRmdDiscoveryStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryStart.setStatus("current")
_TnRmdDiscoverySystemClearTable_Object = MibTable
tnRmdDiscoverySystemClearTable = _TnRmdDiscoverySystemClearTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    tnRmdDiscoverySystemClearTable.setStatus("current")
_TnRmdDiscoverySystemClearEntry_Object = MibTableRow
tnRmdDiscoverySystemClearEntry = _TnRmdDiscoverySystemClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 4, 1)
)
tnRmdDiscoverySystemClearEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnRmdDiscoverySystemClearEntry.setStatus("current")
_TnRmdDiscoveryClear_Type = TruthValue
_TnRmdDiscoveryClear_Object = MibTableColumn
tnRmdDiscoveryClear = _TnRmdDiscoveryClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 4, 1, 1),
    _TnRmdDiscoveryClear_Type()
)
tnRmdDiscoveryClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdDiscoveryClear.setStatus("current")
_TnRmdDiscoveredSystemTable_Object = MibTable
tnRmdDiscoveredSystemTable = _TnRmdDiscoveredSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5)
)
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemTable.setStatus("current")
_TnRmdDiscoveredSystemEntry_Object = MibTableRow
tnRmdDiscoveredSystemEntry = _TnRmdDiscoveredSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1)
)
tnRmdDiscoveredSystemEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdDiscoveredSystemRmdAccessIf"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdDiscoveredSystemMacAddress"),
)
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemEntry.setStatus("current")
_TnRmdDiscoveredSystemRmdAccessIf_Type = TnRmdAccessIfIndex
_TnRmdDiscoveredSystemRmdAccessIf_Object = MibTableColumn
tnRmdDiscoveredSystemRmdAccessIf = _TnRmdDiscoveredSystemRmdAccessIf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 1),
    _TnRmdDiscoveredSystemRmdAccessIf_Type()
)
tnRmdDiscoveredSystemRmdAccessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemRmdAccessIf.setStatus("current")
_TnRmdDiscoveredSystemMacAddress_Type = MacAddress
_TnRmdDiscoveredSystemMacAddress_Object = MibTableColumn
tnRmdDiscoveredSystemMacAddress = _TnRmdDiscoveredSystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 2),
    _TnRmdDiscoveredSystemMacAddress_Type()
)
tnRmdDiscoveredSystemMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemMacAddress.setStatus("current")
_TnRmdDiscoveredSystemDeviceType_Type = TnRmdDeviceType
_TnRmdDiscoveredSystemDeviceType_Object = MibTableColumn
tnRmdDiscoveredSystemDeviceType = _TnRmdDiscoveredSystemDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 3),
    _TnRmdDiscoveredSystemDeviceType_Type()
)
tnRmdDiscoveredSystemDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemDeviceType.setStatus("current")
_TnRmdDiscoveredSystemMcMacAddress_Type = MacAddress
_TnRmdDiscoveredSystemMcMacAddress_Object = MibTableColumn
tnRmdDiscoveredSystemMcMacAddress = _TnRmdDiscoveredSystemMcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 4),
    _TnRmdDiscoveredSystemMcMacAddress_Type()
)
tnRmdDiscoveredSystemMcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemMcMacAddress.setStatus("current")
_TnRmdDiscoveredSystemNumberOfVlanTags_Type = TnRmdNumberOfVlanTags
_TnRmdDiscoveredSystemNumberOfVlanTags_Object = MibTableColumn
tnRmdDiscoveredSystemNumberOfVlanTags = _TnRmdDiscoveredSystemNumberOfVlanTags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 5),
    _TnRmdDiscoveredSystemNumberOfVlanTags_Type()
)
tnRmdDiscoveredSystemNumberOfVlanTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemNumberOfVlanTags.setStatus("current")
_TnRmdDiscoveredSystemOuterTPID_Type = TnRmdTpid
_TnRmdDiscoveredSystemOuterTPID_Object = MibTableColumn
tnRmdDiscoveredSystemOuterTPID = _TnRmdDiscoveredSystemOuterTPID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 6),
    _TnRmdDiscoveredSystemOuterTPID_Type()
)
tnRmdDiscoveredSystemOuterTPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemOuterTPID.setStatus("current")
_TnRmdDiscoveredSystemOuterVlanId_Type = VlanId
_TnRmdDiscoveredSystemOuterVlanId_Object = MibTableColumn
tnRmdDiscoveredSystemOuterVlanId = _TnRmdDiscoveredSystemOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 7),
    _TnRmdDiscoveredSystemOuterVlanId_Type()
)
tnRmdDiscoveredSystemOuterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemOuterVlanId.setStatus("current")
_TnRmdDiscoveredSystemOuterPCP_Type = TnRmdPcp
_TnRmdDiscoveredSystemOuterPCP_Object = MibTableColumn
tnRmdDiscoveredSystemOuterPCP = _TnRmdDiscoveredSystemOuterPCP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 8),
    _TnRmdDiscoveredSystemOuterPCP_Type()
)
tnRmdDiscoveredSystemOuterPCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemOuterPCP.setStatus("current")
_TnRmdDiscoveredSystemOuterDEI_Type = TruthValue
_TnRmdDiscoveredSystemOuterDEI_Object = MibTableColumn
tnRmdDiscoveredSystemOuterDEI = _TnRmdDiscoveredSystemOuterDEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 9),
    _TnRmdDiscoveredSystemOuterDEI_Type()
)
tnRmdDiscoveredSystemOuterDEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemOuterDEI.setStatus("current")
_TnRmdDiscoveredSystemInnerTPID_Type = TnRmdTpid
_TnRmdDiscoveredSystemInnerTPID_Object = MibTableColumn
tnRmdDiscoveredSystemInnerTPID = _TnRmdDiscoveredSystemInnerTPID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 10),
    _TnRmdDiscoveredSystemInnerTPID_Type()
)
tnRmdDiscoveredSystemInnerTPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemInnerTPID.setStatus("current")
_TnRmdDiscoveredSystemInnerVlanId_Type = VlanId
_TnRmdDiscoveredSystemInnerVlanId_Object = MibTableColumn
tnRmdDiscoveredSystemInnerVlanId = _TnRmdDiscoveredSystemInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 11),
    _TnRmdDiscoveredSystemInnerVlanId_Type()
)
tnRmdDiscoveredSystemInnerVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemInnerVlanId.setStatus("current")
_TnRmdDiscoveredSystemInnerPCP_Type = TnRmdPcp
_TnRmdDiscoveredSystemInnerPCP_Object = MibTableColumn
tnRmdDiscoveredSystemInnerPCP = _TnRmdDiscoveredSystemInnerPCP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 12),
    _TnRmdDiscoveredSystemInnerPCP_Type()
)
tnRmdDiscoveredSystemInnerPCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemInnerPCP.setStatus("current")
_TnRmdDiscoveredSystemInnerDEI_Type = TruthValue
_TnRmdDiscoveredSystemInnerDEI_Object = MibTableColumn
tnRmdDiscoveredSystemInnerDEI = _TnRmdDiscoveredSystemInnerDEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 13),
    _TnRmdDiscoveredSystemInnerDEI_Type()
)
tnRmdDiscoveredSystemInnerDEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemInnerDEI.setStatus("current")
_TnRmdDiscoveredSystemOui_Type = TnRmdOui
_TnRmdDiscoveredSystemOui_Object = MibTableColumn
tnRmdDiscoveredSystemOui = _TnRmdDiscoveredSystemOui_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 5, 1, 14),
    _TnRmdDiscoveredSystemOui_Type()
)
tnRmdDiscoveredSystemOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdDiscoveredSystemOui.setStatus("current")
_TnRmdSystemTable_Object = MibTable
tnRmdSystemTable = _TnRmdSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6)
)
if mibBuilder.loadTexts:
    tnRmdSystemTable.setStatus("current")
_TnRmdSystemEntry_Object = MibTableRow
tnRmdSystemEntry = _TnRmdSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1)
)
tnRmdSystemEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
)
if mibBuilder.loadTexts:
    tnRmdSystemEntry.setStatus("current")
_TnRmdSystemId_Type = TnRmdSystemId
_TnRmdSystemId_Object = MibTableColumn
tnRmdSystemId = _TnRmdSystemId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 1),
    _TnRmdSystemId_Type()
)
tnRmdSystemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdSystemId.setStatus("current")
_TnRmdSystemMacAddress_Type = MacAddress
_TnRmdSystemMacAddress_Object = MibTableColumn
tnRmdSystemMacAddress = _TnRmdSystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 2),
    _TnRmdSystemMacAddress_Type()
)
tnRmdSystemMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemMacAddress.setStatus("current")
_TnRmdSystemDeviceType_Type = TnRmdDeviceType
_TnRmdSystemDeviceType_Object = MibTableColumn
tnRmdSystemDeviceType = _TnRmdSystemDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 3),
    _TnRmdSystemDeviceType_Type()
)
tnRmdSystemDeviceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemDeviceType.setStatus("current")
_TnRmdSystemMcMacAddress_Type = MacAddress
_TnRmdSystemMcMacAddress_Object = MibTableColumn
tnRmdSystemMcMacAddress = _TnRmdSystemMcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 4),
    _TnRmdSystemMcMacAddress_Type()
)
tnRmdSystemMcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemMcMacAddress.setStatus("current")
_TnRmdSystemDiscoveryMode_Type = TnRmdDiscoveryMode
_TnRmdSystemDiscoveryMode_Object = MibTableColumn
tnRmdSystemDiscoveryMode = _TnRmdSystemDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 5),
    _TnRmdSystemDiscoveryMode_Type()
)
tnRmdSystemDiscoveryMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemDiscoveryMode.setStatus("current")
_TnRmdSystemNumberOfVlanTags_Type = TnRmdNumberOfVlanTags
_TnRmdSystemNumberOfVlanTags_Object = MibTableColumn
tnRmdSystemNumberOfVlanTags = _TnRmdSystemNumberOfVlanTags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 6),
    _TnRmdSystemNumberOfVlanTags_Type()
)
tnRmdSystemNumberOfVlanTags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemNumberOfVlanTags.setStatus("current")
_TnRmdSystemOuterTPID_Type = TnRmdTpid
_TnRmdSystemOuterTPID_Object = MibTableColumn
tnRmdSystemOuterTPID = _TnRmdSystemOuterTPID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 7),
    _TnRmdSystemOuterTPID_Type()
)
tnRmdSystemOuterTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemOuterTPID.setStatus("current")
_TnRmdSystemOuterVlanId_Type = VlanId
_TnRmdSystemOuterVlanId_Object = MibTableColumn
tnRmdSystemOuterVlanId = _TnRmdSystemOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 8),
    _TnRmdSystemOuterVlanId_Type()
)
tnRmdSystemOuterVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemOuterVlanId.setStatus("current")
_TnRmdSystemOuterPCP_Type = TnRmdPcp
_TnRmdSystemOuterPCP_Object = MibTableColumn
tnRmdSystemOuterPCP = _TnRmdSystemOuterPCP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 9),
    _TnRmdSystemOuterPCP_Type()
)
tnRmdSystemOuterPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemOuterPCP.setStatus("current")
_TnRmdSystemOuterDEI_Type = TruthValue
_TnRmdSystemOuterDEI_Object = MibTableColumn
tnRmdSystemOuterDEI = _TnRmdSystemOuterDEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 10),
    _TnRmdSystemOuterDEI_Type()
)
tnRmdSystemOuterDEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemOuterDEI.setStatus("current")
_TnRmdSystemInnerTPID_Type = TnRmdTpid
_TnRmdSystemInnerTPID_Object = MibTableColumn
tnRmdSystemInnerTPID = _TnRmdSystemInnerTPID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 11),
    _TnRmdSystemInnerTPID_Type()
)
tnRmdSystemInnerTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemInnerTPID.setStatus("current")
_TnRmdSystemInnerVlanId_Type = VlanId
_TnRmdSystemInnerVlanId_Object = MibTableColumn
tnRmdSystemInnerVlanId = _TnRmdSystemInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 12),
    _TnRmdSystemInnerVlanId_Type()
)
tnRmdSystemInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemInnerVlanId.setStatus("current")
_TnRmdSystemInnerPCP_Type = TnRmdPcp
_TnRmdSystemInnerPCP_Object = MibTableColumn
tnRmdSystemInnerPCP = _TnRmdSystemInnerPCP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 13),
    _TnRmdSystemInnerPCP_Type()
)
tnRmdSystemInnerPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemInnerPCP.setStatus("current")
_TnRmdSystemInnerDEI_Type = TruthValue
_TnRmdSystemInnerDEI_Object = MibTableColumn
tnRmdSystemInnerDEI = _TnRmdSystemInnerDEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 14),
    _TnRmdSystemInnerDEI_Type()
)
tnRmdSystemInnerDEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemInnerDEI.setStatus("current")
_TnRmdSystemRmdAccessIf_Type = TnRmdAccessIfIndex
_TnRmdSystemRmdAccessIf_Object = MibTableColumn
tnRmdSystemRmdAccessIf = _TnRmdSystemRmdAccessIf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 15),
    _TnRmdSystemRmdAccessIf_Type()
)
tnRmdSystemRmdAccessIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemRmdAccessIf.setStatus("current")
_TnRmdSystemOui_Type = TnRmdOui
_TnRmdSystemOui_Object = MibTableColumn
tnRmdSystemOui = _TnRmdSystemOui_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 16),
    _TnRmdSystemOui_Type()
)
tnRmdSystemOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemOui.setStatus("current")
_TnRmdSystemName_Type = TnRmdSystemName
_TnRmdSystemName_Object = MibTableColumn
tnRmdSystemName = _TnRmdSystemName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 17),
    _TnRmdSystemName_Type()
)
tnRmdSystemName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemName.setStatus("current")
_TnRmdSystemLocation_Type = TnRmdSystemLocation
_TnRmdSystemLocation_Object = MibTableColumn
tnRmdSystemLocation = _TnRmdSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 18),
    _TnRmdSystemLocation_Type()
)
tnRmdSystemLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemLocation.setStatus("current")
_TnRmdSystemDescription_Type = TItemDescription
_TnRmdSystemDescription_Object = MibTableColumn
tnRmdSystemDescription = _TnRmdSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 19),
    _TnRmdSystemDescription_Type()
)
tnRmdSystemDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemDescription.setStatus("current")
_TnRmdSystemManagementMode_Type = TnRmdSystemManagementMode
_TnRmdSystemManagementMode_Object = MibTableColumn
tnRmdSystemManagementMode = _TnRmdSystemManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 20),
    _TnRmdSystemManagementMode_Type()
)
tnRmdSystemManagementMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemManagementMode.setStatus("current")
_TnRmdSystemReset_Type = TnRmdSystemResetType
_TnRmdSystemReset_Object = MibTableColumn
tnRmdSystemReset = _TnRmdSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 21),
    _TnRmdSystemReset_Type()
)
tnRmdSystemReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemReset.setStatus("current")
_TnRmdSystemRowStatus_Type = RowStatus
_TnRmdSystemRowStatus_Object = MibTableColumn
tnRmdSystemRowStatus = _TnRmdSystemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 22),
    _TnRmdSystemRowStatus_Type()
)
tnRmdSystemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemRowStatus.setStatus("current")
_TnRmdSystemDeviceStatus_Type = TnRmdSystemDeviceStatus
_TnRmdSystemDeviceStatus_Object = MibTableColumn
tnRmdSystemDeviceStatus = _TnRmdSystemDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 6, 1, 23),
    _TnRmdSystemDeviceStatus_Type()
)
tnRmdSystemDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemDeviceStatus.setStatus("current")
_TnRmdSystemInventoryTable_Object = MibTable
tnRmdSystemInventoryTable = _TnRmdSystemInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7)
)
if mibBuilder.loadTexts:
    tnRmdSystemInventoryTable.setStatus("current")
_TnRmdSystemInventoryEntry_Object = MibTableRow
tnRmdSystemInventoryEntry = _TnRmdSystemInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1)
)
tnRmdSystemInventoryEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
)
if mibBuilder.loadTexts:
    tnRmdSystemInventoryEntry.setStatus("current")


class _TnRmdSystemInventoryModuleVendorSerNo_Type(SnmpAdminString):
    """Custom type tnRmdSystemInventoryModuleVendorSerNo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_TnRmdSystemInventoryModuleVendorSerNo_Type.__name__ = "SnmpAdminString"
_TnRmdSystemInventoryModuleVendorSerNo_Object = MibTableColumn
tnRmdSystemInventoryModuleVendorSerNo = _TnRmdSystemInventoryModuleVendorSerNo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 2),
    _TnRmdSystemInventoryModuleVendorSerNo_Type()
)
tnRmdSystemInventoryModuleVendorSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryModuleVendorSerNo.setStatus("current")


class _TnRmdSystemInventoryModuleVendor_Type(SnmpAdminString):
    """Custom type tnRmdSystemInventoryModuleVendor based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnRmdSystemInventoryModuleVendor_Type.__name__ = "SnmpAdminString"
_TnRmdSystemInventoryModuleVendor_Object = MibTableColumn
tnRmdSystemInventoryModuleVendor = _TnRmdSystemInventoryModuleVendor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 3),
    _TnRmdSystemInventoryModuleVendor_Type()
)
tnRmdSystemInventoryModuleVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryModuleVendor.setStatus("current")
_TnRmdSystemInventoryWavelength_Type = Unsigned32
_TnRmdSystemInventoryWavelength_Object = MibTableColumn
tnRmdSystemInventoryWavelength = _TnRmdSystemInventoryWavelength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 4),
    _TnRmdSystemInventoryWavelength_Type()
)
tnRmdSystemInventoryWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryWavelength.setStatus("current")
_TnRmdSystemInventoryModuleType_Type = SnmpAdminString
_TnRmdSystemInventoryModuleType_Object = MibTableColumn
tnRmdSystemInventoryModuleType = _TnRmdSystemInventoryModuleType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 5),
    _TnRmdSystemInventoryModuleType_Type()
)
tnRmdSystemInventoryModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryModuleType.setStatus("current")
_TnRmdSystemInventoryCLEI_Type = SnmpAdminString
_TnRmdSystemInventoryCLEI_Object = MibTableColumn
tnRmdSystemInventoryCLEI = _TnRmdSystemInventoryCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 6),
    _TnRmdSystemInventoryCLEI_Type()
)
tnRmdSystemInventoryCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryCLEI.setStatus("current")
_TnRmdSystemInventoryUnitPartNum_Type = SnmpAdminString
_TnRmdSystemInventoryUnitPartNum_Object = MibTableColumn
tnRmdSystemInventoryUnitPartNum = _TnRmdSystemInventoryUnitPartNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 7),
    _TnRmdSystemInventoryUnitPartNum_Type()
)
tnRmdSystemInventoryUnitPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryUnitPartNum.setStatus("current")
_TnRmdSystemInventorySWPartNum_Type = SnmpAdminString
_TnRmdSystemInventorySWPartNum_Object = MibTableColumn
tnRmdSystemInventorySWPartNum = _TnRmdSystemInventorySWPartNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 8),
    _TnRmdSystemInventorySWPartNum_Type()
)
tnRmdSystemInventorySWPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventorySWPartNum.setStatus("current")
_TnRmdSystemInventoryFactoryID_Type = SnmpAdminString
_TnRmdSystemInventoryFactoryID_Object = MibTableColumn
tnRmdSystemInventoryFactoryID = _TnRmdSystemInventoryFactoryID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 9),
    _TnRmdSystemInventoryFactoryID_Type()
)
tnRmdSystemInventoryFactoryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryFactoryID.setStatus("current")
_TnRmdSystemInventoryDate_Type = SnmpAdminString
_TnRmdSystemInventoryDate_Object = MibTableColumn
tnRmdSystemInventoryDate = _TnRmdSystemInventoryDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 10),
    _TnRmdSystemInventoryDate_Type()
)
tnRmdSystemInventoryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryDate.setStatus("current")
_TnRmdSystemInventoryExtraData_Type = SnmpAdminString
_TnRmdSystemInventoryExtraData_Object = MibTableColumn
tnRmdSystemInventoryExtraData = _TnRmdSystemInventoryExtraData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 11),
    _TnRmdSystemInventoryExtraData_Type()
)
tnRmdSystemInventoryExtraData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryExtraData.setStatus("current")
_TnRmdSystemInventoryMaximumCaseTemperature_Type = Integer32
_TnRmdSystemInventoryMaximumCaseTemperature_Object = MibTableColumn
tnRmdSystemInventoryMaximumCaseTemperature = _TnRmdSystemInventoryMaximumCaseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 12),
    _TnRmdSystemInventoryMaximumCaseTemperature_Type()
)
tnRmdSystemInventoryMaximumCaseTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryMaximumCaseTemperature.setStatus("current")


class _TnRmdSystemInventoryInterchangeabilityMarking_Type(SnmpAdminString):
    """Custom type tnRmdSystemInventoryInterchangeabilityMarking based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_TnRmdSystemInventoryInterchangeabilityMarking_Type.__name__ = "SnmpAdminString"
_TnRmdSystemInventoryInterchangeabilityMarking_Object = MibTableColumn
tnRmdSystemInventoryInterchangeabilityMarking = _TnRmdSystemInventoryInterchangeabilityMarking_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 13),
    _TnRmdSystemInventoryInterchangeabilityMarking_Type()
)
tnRmdSystemInventoryInterchangeabilityMarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryInterchangeabilityMarking.setStatus("current")


class _TnRmdSystemInventoryAcronymCode_Type(SnmpAdminString):
    """Custom type tnRmdSystemInventoryAcronymCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnRmdSystemInventoryAcronymCode_Type.__name__ = "SnmpAdminString"
_TnRmdSystemInventoryAcronymCode_Object = MibTableColumn
tnRmdSystemInventoryAcronymCode = _TnRmdSystemInventoryAcronymCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 14),
    _TnRmdSystemInventoryAcronymCode_Type()
)
tnRmdSystemInventoryAcronymCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryAcronymCode.setStatus("current")


class _TnRmdSystemInventoryCustomerInventoryField_Type(SnmpAdminString):
    """Custom type tnRmdSystemInventoryCustomerInventoryField based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnRmdSystemInventoryCustomerInventoryField_Type.__name__ = "SnmpAdminString"
_TnRmdSystemInventoryCustomerInventoryField_Object = MibTableColumn
tnRmdSystemInventoryCustomerInventoryField = _TnRmdSystemInventoryCustomerInventoryField_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 7, 1, 15),
    _TnRmdSystemInventoryCustomerInventoryField_Type()
)
tnRmdSystemInventoryCustomerInventoryField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemInventoryCustomerInventoryField.setStatus("current")
_TnRmdSystemSwImageTable_Object = MibTable
tnRmdSystemSwImageTable = _TnRmdSystemSwImageTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 8)
)
if mibBuilder.loadTexts:
    tnRmdSystemSwImageTable.setStatus("current")
_TnRmdSystemSwImageEntry_Object = MibTableRow
tnRmdSystemSwImageEntry = _TnRmdSystemSwImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 8, 1)
)
tnRmdSystemSwImageEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemSwImageId"),
)
if mibBuilder.loadTexts:
    tnRmdSystemSwImageEntry.setStatus("current")
_TnRmdSystemSwImageId_Type = Unsigned32
_TnRmdSystemSwImageId_Object = MibTableColumn
tnRmdSystemSwImageId = _TnRmdSystemSwImageId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 8, 1, 1),
    _TnRmdSystemSwImageId_Type()
)
tnRmdSystemSwImageId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdSystemSwImageId.setStatus("current")
_TnRmdSystemSwImageState_Type = TnRmdSwImageState
_TnRmdSystemSwImageState_Object = MibTableColumn
tnRmdSystemSwImageState = _TnRmdSystemSwImageState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 8, 1, 2),
    _TnRmdSystemSwImageState_Type()
)
tnRmdSystemSwImageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemSwImageState.setStatus("current")
_TnRmdSystemSwImageVersion_Type = TnRmdVersion
_TnRmdSystemSwImageVersion_Object = MibTableColumn
tnRmdSystemSwImageVersion = _TnRmdSystemSwImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 8, 1, 3),
    _TnRmdSystemSwImageVersion_Type()
)
tnRmdSystemSwImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemSwImageVersion.setStatus("current")
_TnRmdSystemSwImageDate_Type = DateAndTime
_TnRmdSystemSwImageDate_Object = MibTableColumn
tnRmdSystemSwImageDate = _TnRmdSystemSwImageDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 8, 1, 4),
    _TnRmdSystemSwImageDate_Type()
)
tnRmdSystemSwImageDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemSwImageDate.setStatus("current")
_TnRmdSystemSwImageItemCode_Type = TnRmdItemCode
_TnRmdSystemSwImageItemCode_Object = MibTableColumn
tnRmdSystemSwImageItemCode = _TnRmdSystemSwImageItemCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 8, 1, 5),
    _TnRmdSystemSwImageItemCode_Type()
)
tnRmdSystemSwImageItemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemSwImageItemCode.setStatus("current")
_TnRmdSystemSwImageSize_Type = Unsigned32
_TnRmdSystemSwImageSize_Object = MibTableColumn
tnRmdSystemSwImageSize = _TnRmdSystemSwImageSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 8, 1, 6),
    _TnRmdSystemSwImageSize_Type()
)
tnRmdSystemSwImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemSwImageSize.setStatus("current")
_TnRmdSystemFwVersionTable_Object = MibTable
tnRmdSystemFwVersionTable = _TnRmdSystemFwVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 9)
)
if mibBuilder.loadTexts:
    tnRmdSystemFwVersionTable.setStatus("current")
_TnRmdSystemFwVersionEntry_Object = MibTableRow
tnRmdSystemFwVersionEntry = _TnRmdSystemFwVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 9, 1)
)
tnRmdSystemFwVersionEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
)
if mibBuilder.loadTexts:
    tnRmdSystemFwVersionEntry.setStatus("current")
_TnRmdSystemFirmwareVersion_Type = TnRmdVersion
_TnRmdSystemFirmwareVersion_Object = MibTableColumn
tnRmdSystemFirmwareVersion = _TnRmdSystemFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 9, 1, 1),
    _TnRmdSystemFirmwareVersion_Type()
)
tnRmdSystemFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemFirmwareVersion.setStatus("current")
_TnRmdSystemPpVersion_Type = TnRmdVersion
_TnRmdSystemPpVersion_Object = MibTableColumn
tnRmdSystemPpVersion = _TnRmdSystemPpVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 9, 1, 2),
    _TnRmdSystemPpVersion_Type()
)
tnRmdSystemPpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemPpVersion.setStatus("current")
_TnRmdSystemPpNvmVersion_Type = TnRmdVersion
_TnRmdSystemPpNvmVersion_Object = MibTableColumn
tnRmdSystemPpNvmVersion = _TnRmdSystemPpNvmVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 9, 1, 3),
    _TnRmdSystemPpNvmVersion_Type()
)
tnRmdSystemPpNvmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemPpNvmVersion.setStatus("current")
_TnRmdSystemRmdAccessIfTable_Object = MibTable
tnRmdSystemRmdAccessIfTable = _TnRmdSystemRmdAccessIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 12)
)
if mibBuilder.loadTexts:
    tnRmdSystemRmdAccessIfTable.setStatus("current")
_TnRmdSystemRmdAccessIfEntry_Object = MibTableRow
tnRmdSystemRmdAccessIfEntry = _TnRmdSystemRmdAccessIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 12, 1)
)
tnRmdSystemRmdAccessIfEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemRmdAccessIfIndex"),
)
if mibBuilder.loadTexts:
    tnRmdSystemRmdAccessIfEntry.setStatus("current")
_TnRmdSystemRmdAccessIfIndex_Type = TnRmdAccessIfIndex
_TnRmdSystemRmdAccessIfIndex_Object = MibTableColumn
tnRmdSystemRmdAccessIfIndex = _TnRmdSystemRmdAccessIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 12, 1, 1),
    _TnRmdSystemRmdAccessIfIndex_Type()
)
tnRmdSystemRmdAccessIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdSystemRmdAccessIfIndex.setStatus("current")
_TnRmdSystemRmdAccessIfRowStatus_Type = RowStatus
_TnRmdSystemRmdAccessIfRowStatus_Object = MibTableColumn
tnRmdSystemRmdAccessIfRowStatus = _TnRmdSystemRmdAccessIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 12, 1, 2),
    _TnRmdSystemRmdAccessIfRowStatus_Type()
)
tnRmdSystemRmdAccessIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemRmdAccessIfRowStatus.setStatus("current")
_TnRmdSystemRmdAccessIfType_Type = TnRmdSystemRmdAccessIfType
_TnRmdSystemRmdAccessIfType_Object = MibTableColumn
tnRmdSystemRmdAccessIfType = _TnRmdSystemRmdAccessIfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 12, 1, 3),
    _TnRmdSystemRmdAccessIfType_Type()
)
tnRmdSystemRmdAccessIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemRmdAccessIfType.setStatus("current")
_TnRmdSystemRmdAccessIfPortId_Type = TmnxPortID
_TnRmdSystemRmdAccessIfPortId_Object = MibTableColumn
tnRmdSystemRmdAccessIfPortId = _TnRmdSystemRmdAccessIfPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 12, 1, 4),
    _TnRmdSystemRmdAccessIfPortId_Type()
)
tnRmdSystemRmdAccessIfPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemRmdAccessIfPortId.setStatus("current")
_TnRmdSystemRmdAccessIfEncapVal_Type = TmnxEncapVal
_TnRmdSystemRmdAccessIfEncapVal_Object = MibTableColumn
tnRmdSystemRmdAccessIfEncapVal = _TnRmdSystemRmdAccessIfEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 12, 1, 5),
    _TnRmdSystemRmdAccessIfEncapVal_Type()
)
tnRmdSystemRmdAccessIfEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemRmdAccessIfEncapVal.setStatus("current")
_TnRmdSystemRmdAccessIfPortIdExt_Type = TmnxPortID
_TnRmdSystemRmdAccessIfPortIdExt_Object = MibTableColumn
tnRmdSystemRmdAccessIfPortIdExt = _TnRmdSystemRmdAccessIfPortIdExt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 12, 1, 6),
    _TnRmdSystemRmdAccessIfPortIdExt_Type()
)
tnRmdSystemRmdAccessIfPortIdExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemRmdAccessIfPortIdExt.setStatus("current")
_TnRmdSystemRmdAccessIfEncapValExt_Type = TmnxEncapVal
_TnRmdSystemRmdAccessIfEncapValExt_Object = MibTableColumn
tnRmdSystemRmdAccessIfEncapValExt = _TnRmdSystemRmdAccessIfEncapValExt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 4, 12, 1, 7),
    _TnRmdSystemRmdAccessIfEncapValExt_Type()
)
tnRmdSystemRmdAccessIfEncapValExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdSystemRmdAccessIfEncapValExt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-RMD-SYSTEM-MIB",
    **{"TnRmdDeviceType": TnRmdDeviceType,
       "TnRmdDiscoveryMode": TnRmdDiscoveryMode,
       "TnRmdNumberOfVlanTags": TnRmdNumberOfVlanTags,
       "TnRmdSwImageState": TnRmdSwImageState,
       "TnRmdSystemId": TnRmdSystemId,
       "TnRmdSystemLocation": TnRmdSystemLocation,
       "TnRmdSystemManagementMode": TnRmdSystemManagementMode,
       "TnRmdSystemName": TnRmdSystemName,
       "TnRmdSystemResetType": TnRmdSystemResetType,
       "TnRmdSystemDeviceStatus": TnRmdSystemDeviceStatus,
       "TnRmdSystemRmdAccessIfType": TnRmdSystemRmdAccessIfType,
       "tnRmdSystemMibModule": tnRmdSystemMibModule,
       "tnRmdSystemObjects": tnRmdSystemObjects,
       "tnRmdSystemAttributeTotal": tnRmdSystemAttributeTotal,
       "tnRmdDiscoverySystemTable": tnRmdDiscoverySystemTable,
       "tnRmdDiscoverySystemEntry": tnRmdDiscoverySystemEntry,
       "tnRmdDiscoveryMcMacAddress": tnRmdDiscoveryMcMacAddress,
       "tnRmdDiscoveryMode": tnRmdDiscoveryMode,
       "tnRmdDiscoveryNumberOfVlanTags": tnRmdDiscoveryNumberOfVlanTags,
       "tnRmdDiscoveryOuterTPID": tnRmdDiscoveryOuterTPID,
       "tnRmdDiscoveryOuterVlanId": tnRmdDiscoveryOuterVlanId,
       "tnRmdDiscoveryOuterPCP": tnRmdDiscoveryOuterPCP,
       "tnRmdDiscoveryOuterDEI": tnRmdDiscoveryOuterDEI,
       "tnRmdDiscoveryInnerTPID": tnRmdDiscoveryInnerTPID,
       "tnRmdDiscoveryInnerVlanId": tnRmdDiscoveryInnerVlanId,
       "tnRmdDiscoveryInnerPCP": tnRmdDiscoveryInnerPCP,
       "tnRmdDiscoveryInnerDEI": tnRmdDiscoveryInnerDEI,
       "tnRmdDiscoveryRmdAccessIf": tnRmdDiscoveryRmdAccessIf,
       "tnRmdDiscoveryOui": tnRmdDiscoveryOui,
       "tnRmdDiscoverySystemStartTable": tnRmdDiscoverySystemStartTable,
       "tnRmdDiscoverySystemStartEntry": tnRmdDiscoverySystemStartEntry,
       "tnRmdDiscoveryStart": tnRmdDiscoveryStart,
       "tnRmdDiscoverySystemClearTable": tnRmdDiscoverySystemClearTable,
       "tnRmdDiscoverySystemClearEntry": tnRmdDiscoverySystemClearEntry,
       "tnRmdDiscoveryClear": tnRmdDiscoveryClear,
       "tnRmdDiscoveredSystemTable": tnRmdDiscoveredSystemTable,
       "tnRmdDiscoveredSystemEntry": tnRmdDiscoveredSystemEntry,
       "tnRmdDiscoveredSystemRmdAccessIf": tnRmdDiscoveredSystemRmdAccessIf,
       "tnRmdDiscoveredSystemMacAddress": tnRmdDiscoveredSystemMacAddress,
       "tnRmdDiscoveredSystemDeviceType": tnRmdDiscoveredSystemDeviceType,
       "tnRmdDiscoveredSystemMcMacAddress": tnRmdDiscoveredSystemMcMacAddress,
       "tnRmdDiscoveredSystemNumberOfVlanTags": tnRmdDiscoveredSystemNumberOfVlanTags,
       "tnRmdDiscoveredSystemOuterTPID": tnRmdDiscoveredSystemOuterTPID,
       "tnRmdDiscoveredSystemOuterVlanId": tnRmdDiscoveredSystemOuterVlanId,
       "tnRmdDiscoveredSystemOuterPCP": tnRmdDiscoveredSystemOuterPCP,
       "tnRmdDiscoveredSystemOuterDEI": tnRmdDiscoveredSystemOuterDEI,
       "tnRmdDiscoveredSystemInnerTPID": tnRmdDiscoveredSystemInnerTPID,
       "tnRmdDiscoveredSystemInnerVlanId": tnRmdDiscoveredSystemInnerVlanId,
       "tnRmdDiscoveredSystemInnerPCP": tnRmdDiscoveredSystemInnerPCP,
       "tnRmdDiscoveredSystemInnerDEI": tnRmdDiscoveredSystemInnerDEI,
       "tnRmdDiscoveredSystemOui": tnRmdDiscoveredSystemOui,
       "tnRmdSystemTable": tnRmdSystemTable,
       "tnRmdSystemEntry": tnRmdSystemEntry,
       "tnRmdSystemId": tnRmdSystemId,
       "tnRmdSystemMacAddress": tnRmdSystemMacAddress,
       "tnRmdSystemDeviceType": tnRmdSystemDeviceType,
       "tnRmdSystemMcMacAddress": tnRmdSystemMcMacAddress,
       "tnRmdSystemDiscoveryMode": tnRmdSystemDiscoveryMode,
       "tnRmdSystemNumberOfVlanTags": tnRmdSystemNumberOfVlanTags,
       "tnRmdSystemOuterTPID": tnRmdSystemOuterTPID,
       "tnRmdSystemOuterVlanId": tnRmdSystemOuterVlanId,
       "tnRmdSystemOuterPCP": tnRmdSystemOuterPCP,
       "tnRmdSystemOuterDEI": tnRmdSystemOuterDEI,
       "tnRmdSystemInnerTPID": tnRmdSystemInnerTPID,
       "tnRmdSystemInnerVlanId": tnRmdSystemInnerVlanId,
       "tnRmdSystemInnerPCP": tnRmdSystemInnerPCP,
       "tnRmdSystemInnerDEI": tnRmdSystemInnerDEI,
       "tnRmdSystemRmdAccessIf": tnRmdSystemRmdAccessIf,
       "tnRmdSystemOui": tnRmdSystemOui,
       "tnRmdSystemName": tnRmdSystemName,
       "tnRmdSystemLocation": tnRmdSystemLocation,
       "tnRmdSystemDescription": tnRmdSystemDescription,
       "tnRmdSystemManagementMode": tnRmdSystemManagementMode,
       "tnRmdSystemReset": tnRmdSystemReset,
       "tnRmdSystemRowStatus": tnRmdSystemRowStatus,
       "tnRmdSystemDeviceStatus": tnRmdSystemDeviceStatus,
       "tnRmdSystemInventoryTable": tnRmdSystemInventoryTable,
       "tnRmdSystemInventoryEntry": tnRmdSystemInventoryEntry,
       "tnRmdSystemInventoryModuleVendorSerNo": tnRmdSystemInventoryModuleVendorSerNo,
       "tnRmdSystemInventoryModuleVendor": tnRmdSystemInventoryModuleVendor,
       "tnRmdSystemInventoryWavelength": tnRmdSystemInventoryWavelength,
       "tnRmdSystemInventoryModuleType": tnRmdSystemInventoryModuleType,
       "tnRmdSystemInventoryCLEI": tnRmdSystemInventoryCLEI,
       "tnRmdSystemInventoryUnitPartNum": tnRmdSystemInventoryUnitPartNum,
       "tnRmdSystemInventorySWPartNum": tnRmdSystemInventorySWPartNum,
       "tnRmdSystemInventoryFactoryID": tnRmdSystemInventoryFactoryID,
       "tnRmdSystemInventoryDate": tnRmdSystemInventoryDate,
       "tnRmdSystemInventoryExtraData": tnRmdSystemInventoryExtraData,
       "tnRmdSystemInventoryMaximumCaseTemperature": tnRmdSystemInventoryMaximumCaseTemperature,
       "tnRmdSystemInventoryInterchangeabilityMarking": tnRmdSystemInventoryInterchangeabilityMarking,
       "tnRmdSystemInventoryAcronymCode": tnRmdSystemInventoryAcronymCode,
       "tnRmdSystemInventoryCustomerInventoryField": tnRmdSystemInventoryCustomerInventoryField,
       "tnRmdSystemSwImageTable": tnRmdSystemSwImageTable,
       "tnRmdSystemSwImageEntry": tnRmdSystemSwImageEntry,
       "tnRmdSystemSwImageId": tnRmdSystemSwImageId,
       "tnRmdSystemSwImageState": tnRmdSystemSwImageState,
       "tnRmdSystemSwImageVersion": tnRmdSystemSwImageVersion,
       "tnRmdSystemSwImageDate": tnRmdSystemSwImageDate,
       "tnRmdSystemSwImageItemCode": tnRmdSystemSwImageItemCode,
       "tnRmdSystemSwImageSize": tnRmdSystemSwImageSize,
       "tnRmdSystemFwVersionTable": tnRmdSystemFwVersionTable,
       "tnRmdSystemFwVersionEntry": tnRmdSystemFwVersionEntry,
       "tnRmdSystemFirmwareVersion": tnRmdSystemFirmwareVersion,
       "tnRmdSystemPpVersion": tnRmdSystemPpVersion,
       "tnRmdSystemPpNvmVersion": tnRmdSystemPpNvmVersion,
       "tnRmdSystemRmdAccessIfTable": tnRmdSystemRmdAccessIfTable,
       "tnRmdSystemRmdAccessIfEntry": tnRmdSystemRmdAccessIfEntry,
       "tnRmdSystemRmdAccessIfIndex": tnRmdSystemRmdAccessIfIndex,
       "tnRmdSystemRmdAccessIfRowStatus": tnRmdSystemRmdAccessIfRowStatus,
       "tnRmdSystemRmdAccessIfType": tnRmdSystemRmdAccessIfType,
       "tnRmdSystemRmdAccessIfPortId": tnRmdSystemRmdAccessIfPortId,
       "tnRmdSystemRmdAccessIfEncapVal": tnRmdSystemRmdAccessIfEncapVal,
       "tnRmdSystemRmdAccessIfPortIdExt": tnRmdSystemRmdAccessIfPortIdExt,
       "tnRmdSystemRmdAccessIfEncapValExt": tnRmdSystemRmdAccessIfEncapValExt}
)
