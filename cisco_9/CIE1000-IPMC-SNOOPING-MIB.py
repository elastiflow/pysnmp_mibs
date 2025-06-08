# SNMP MIB module (CIE1000-IPMC-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-IPMC-SNOOPING-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:41 2025
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

(CIE1000DisplayString,
 CIE1000InterfaceIndex,
 CIE1000PortList,
 CIE1000RowEditorState,
 CIE1000Unsigned8) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000InterfaceIndex",
    "CIE1000PortList",
    "CIE1000RowEditorState",
    "CIE1000Unsigned8")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000IpmcSnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingMib.setRevisions(
        ("2014-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000IpmcSnoopingIgmpGroupSrcListGroupFilterModeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 0),
          ("include", 1),
          ("none", 2))
    )



class CIE1000IpmcSnoopingIgmpGroupSrcListSourceTypeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )



class CIE1000IpmcSnoopingIgmpInterfaceCompatibilityEnum(TextualConvention, Integer32):
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
        *(("auto", 0),
          ("igmpv1", 1),
          ("igmpv2", 2),
          ("igmpv3", 3))
    )



class CIE1000IpmcSnoopingIgmpRouterPortStatusEnum(TextualConvention, Integer32):
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
        *(("none", 0),
          ("static", 1),
          ("dynamic", 2),
          ("both", 3))
    )



class CIE1000IpmcSnoopingIgmpVlanStatusQuerierStatusEnum(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("initial", 1),
          ("idle", 2),
          ("active", 3))
    )



class CIE1000IpmcSnoopingMldGroupSrcListGroupFilterModeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 0),
          ("include", 1),
          ("none", 2))
    )



class CIE1000IpmcSnoopingMldGroupSrcListSourceEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )



class CIE1000IpmcSnoopingMldInterfaceCompatibilityEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("mldv1", 1),
          ("mldv2", 2))
    )



class CIE1000IpmcSnoopingMldRouterPortStatusEnum(TextualConvention, Integer32):
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
        *(("none", 0),
          ("static", 1),
          ("dynamic", 2),
          ("both", 3))
    )



class CIE1000IpmcSnoopingMldVlanStatusQuerierStatusEnum(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("initial", 1),
          ("idle", 2),
          ("active", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000IpmcSnoopingMibObjects_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingMibObjects = _Cie1000IpmcSnoopingMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1)
)
_Cie1000IpmcSnoopingConfig_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingConfig = _Cie1000IpmcSnoopingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2)
)
_Cie1000IpmcSnoopingConfigIgmpGlobals_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingConfigIgmpGlobals = _Cie1000IpmcSnoopingConfigIgmpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 1)
)
_Cie1000IpmcSnoopingConfigIgmpGlobalsAdminState_Type = TruthValue
_Cie1000IpmcSnoopingConfigIgmpGlobalsAdminState_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpGlobalsAdminState = _Cie1000IpmcSnoopingConfigIgmpGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 1, 1),
    _Cie1000IpmcSnoopingConfigIgmpGlobalsAdminState_Type()
)
cie1000IpmcSnoopingConfigIgmpGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpGlobalsAdminState.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpGlobalsUnregisteredFlooding_Type = TruthValue
_Cie1000IpmcSnoopingConfigIgmpGlobalsUnregisteredFlooding_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpGlobalsUnregisteredFlooding = _Cie1000IpmcSnoopingConfigIgmpGlobalsUnregisteredFlooding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 1, 2),
    _Cie1000IpmcSnoopingConfigIgmpGlobalsUnregisteredFlooding_Type()
)
cie1000IpmcSnoopingConfigIgmpGlobalsUnregisteredFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpGlobalsUnregisteredFlooding.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeAddress_Type = IpAddress
_Cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeAddress_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeAddress = _Cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 1, 3),
    _Cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeAddress_Type()
)
cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeAddress.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeMask_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeMask_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeMask = _Cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 1, 4),
    _Cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeMask_Type()
)
cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeMask.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpGlobalsProxy_Type = TruthValue
_Cie1000IpmcSnoopingConfigIgmpGlobalsProxy_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpGlobalsProxy = _Cie1000IpmcSnoopingConfigIgmpGlobalsProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 1, 5),
    _Cie1000IpmcSnoopingConfigIgmpGlobalsProxy_Type()
)
cie1000IpmcSnoopingConfigIgmpGlobalsProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpGlobalsProxy.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpGlobalsLeaveProxy_Type = TruthValue
_Cie1000IpmcSnoopingConfigIgmpGlobalsLeaveProxy_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpGlobalsLeaveProxy = _Cie1000IpmcSnoopingConfigIgmpGlobalsLeaveProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 1, 6),
    _Cie1000IpmcSnoopingConfigIgmpGlobalsLeaveProxy_Type()
)
cie1000IpmcSnoopingConfigIgmpGlobalsLeaveProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpGlobalsLeaveProxy.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpPortTable_Object = MibTable
cie1000IpmcSnoopingConfigIgmpPortTable = _Cie1000IpmcSnoopingConfigIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpPortTable.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpPortEntry_Object = MibTableRow
cie1000IpmcSnoopingConfigIgmpPortEntry = _Cie1000IpmcSnoopingConfigIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 2, 1)
)
cie1000IpmcSnoopingConfigIgmpPortEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpPortPortIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpPortEntry.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpPortPortIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingConfigIgmpPortPortIndex_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpPortPortIndex = _Cie1000IpmcSnoopingConfigIgmpPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 2, 1, 1),
    _Cie1000IpmcSnoopingConfigIgmpPortPortIndex_Type()
)
cie1000IpmcSnoopingConfigIgmpPortPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpPortPortIndex.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpPortAsRouterPort_Type = TruthValue
_Cie1000IpmcSnoopingConfigIgmpPortAsRouterPort_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpPortAsRouterPort = _Cie1000IpmcSnoopingConfigIgmpPortAsRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 2, 1, 2),
    _Cie1000IpmcSnoopingConfigIgmpPortAsRouterPort_Type()
)
cie1000IpmcSnoopingConfigIgmpPortAsRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpPortAsRouterPort.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpPortDoFastLeave_Type = TruthValue
_Cie1000IpmcSnoopingConfigIgmpPortDoFastLeave_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpPortDoFastLeave = _Cie1000IpmcSnoopingConfigIgmpPortDoFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 2, 1, 3),
    _Cie1000IpmcSnoopingConfigIgmpPortDoFastLeave_Type()
)
cie1000IpmcSnoopingConfigIgmpPortDoFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpPortDoFastLeave.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpPortThrottlingNumber_Type = Integer32
_Cie1000IpmcSnoopingConfigIgmpPortThrottlingNumber_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpPortThrottlingNumber = _Cie1000IpmcSnoopingConfigIgmpPortThrottlingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 2, 1, 4),
    _Cie1000IpmcSnoopingConfigIgmpPortThrottlingNumber_Type()
)
cie1000IpmcSnoopingConfigIgmpPortThrottlingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpPortThrottlingNumber.setStatus("current")


class _Cie1000IpmcSnoopingConfigIgmpPortFilteringProfile_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcSnoopingConfigIgmpPortFilteringProfile based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcSnoopingConfigIgmpPortFilteringProfile_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcSnoopingConfigIgmpPortFilteringProfile_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpPortFilteringProfile = _Cie1000IpmcSnoopingConfigIgmpPortFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 2, 1, 5),
    _Cie1000IpmcSnoopingConfigIgmpPortFilteringProfile_Type()
)
cie1000IpmcSnoopingConfigIgmpPortFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpPortFilteringProfile.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTable_Object = MibTable
cie1000IpmcSnoopingConfigIgmpIfTable = _Cie1000IpmcSnoopingConfigIgmpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTable.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfEntry_Object = MibTableRow
cie1000IpmcSnoopingConfigIgmpIfEntry = _Cie1000IpmcSnoopingConfigIgmpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1)
)
cie1000IpmcSnoopingConfigIgmpIfEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfEntry.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingConfigIgmpIfIfIndex_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfIfIndex = _Cie1000IpmcSnoopingConfigIgmpIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 1),
    _Cie1000IpmcSnoopingConfigIgmpIfIfIndex_Type()
)
cie1000IpmcSnoopingConfigIgmpIfIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfIfIndex.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfAdminState_Type = TruthValue
_Cie1000IpmcSnoopingConfigIgmpIfAdminState_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfAdminState = _Cie1000IpmcSnoopingConfigIgmpIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 2),
    _Cie1000IpmcSnoopingConfigIgmpIfAdminState_Type()
)
cie1000IpmcSnoopingConfigIgmpIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfAdminState.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfQuerierElection_Type = TruthValue
_Cie1000IpmcSnoopingConfigIgmpIfQuerierElection_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfQuerierElection = _Cie1000IpmcSnoopingConfigIgmpIfQuerierElection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 3),
    _Cie1000IpmcSnoopingConfigIgmpIfQuerierElection_Type()
)
cie1000IpmcSnoopingConfigIgmpIfQuerierElection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfQuerierElection.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfQuerierAddress_Type = IpAddress
_Cie1000IpmcSnoopingConfigIgmpIfQuerierAddress_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfQuerierAddress = _Cie1000IpmcSnoopingConfigIgmpIfQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 4),
    _Cie1000IpmcSnoopingConfigIgmpIfQuerierAddress_Type()
)
cie1000IpmcSnoopingConfigIgmpIfQuerierAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfQuerierAddress.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfCompatibility_Type = CIE1000IpmcSnoopingIgmpInterfaceCompatibilityEnum
_Cie1000IpmcSnoopingConfigIgmpIfCompatibility_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfCompatibility = _Cie1000IpmcSnoopingConfigIgmpIfCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 5),
    _Cie1000IpmcSnoopingConfigIgmpIfCompatibility_Type()
)
cie1000IpmcSnoopingConfigIgmpIfCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfCompatibility.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfPriority_Type = CIE1000Unsigned8
_Cie1000IpmcSnoopingConfigIgmpIfPriority_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfPriority = _Cie1000IpmcSnoopingConfigIgmpIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 6),
    _Cie1000IpmcSnoopingConfigIgmpIfPriority_Type()
)
cie1000IpmcSnoopingConfigIgmpIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfPriority.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfRv_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpIfRv_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfRv = _Cie1000IpmcSnoopingConfigIgmpIfRv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 7),
    _Cie1000IpmcSnoopingConfigIgmpIfRv_Type()
)
cie1000IpmcSnoopingConfigIgmpIfRv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfRv.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfQi_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpIfQi_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfQi = _Cie1000IpmcSnoopingConfigIgmpIfQi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 8),
    _Cie1000IpmcSnoopingConfigIgmpIfQi_Type()
)
cie1000IpmcSnoopingConfigIgmpIfQi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfQi.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfQri_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpIfQri_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfQri = _Cie1000IpmcSnoopingConfigIgmpIfQri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 9),
    _Cie1000IpmcSnoopingConfigIgmpIfQri_Type()
)
cie1000IpmcSnoopingConfigIgmpIfQri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfQri.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfLmqi_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpIfLmqi_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfLmqi = _Cie1000IpmcSnoopingConfigIgmpIfLmqi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 10),
    _Cie1000IpmcSnoopingConfigIgmpIfLmqi_Type()
)
cie1000IpmcSnoopingConfigIgmpIfLmqi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfLmqi.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfUri_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpIfUri_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfUri = _Cie1000IpmcSnoopingConfigIgmpIfUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 11),
    _Cie1000IpmcSnoopingConfigIgmpIfUri_Type()
)
cie1000IpmcSnoopingConfigIgmpIfUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfUri.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfAction_Type = CIE1000RowEditorState
_Cie1000IpmcSnoopingConfigIgmpIfAction_Object = MibTableColumn
cie1000IpmcSnoopingConfigIgmpIfAction = _Cie1000IpmcSnoopingConfigIgmpIfAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 3, 1, 100),
    _Cie1000IpmcSnoopingConfigIgmpIfAction_Type()
)
cie1000IpmcSnoopingConfigIgmpIfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfAction.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingConfigIgmpIfTableRowEditor = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4)
)
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorIfIndex_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorIfIndex = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 1),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorIfIndex_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorIfIndex.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAdminState_Type = TruthValue
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAdminState_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAdminState = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 2),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAdminState_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAdminState.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierElection_Type = TruthValue
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierElection_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierElection = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierElection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 3),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierElection_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierElection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierElection.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierAddress_Type = IpAddress
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierAddress_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierAddress = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 4),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierAddress_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierAddress.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorCompatibility_Type = CIE1000IpmcSnoopingIgmpInterfaceCompatibilityEnum
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorCompatibility_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorCompatibility = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 5),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorCompatibility_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorCompatibility.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorPriority_Type = CIE1000Unsigned8
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorPriority_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorPriority = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 6),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorPriority_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorPriority.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorRv_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorRv_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorRv = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorRv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 7),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorRv_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorRv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorRv.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQi_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQi_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQi = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 8),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQi_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQi.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQri_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQri_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQri = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 9),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQri_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQri.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorLmqi_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorLmqi_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorLmqi = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorLmqi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 10),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorLmqi_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorLmqi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorLmqi.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorUri_Type = Unsigned32
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorUri_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorUri = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 11),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorUri_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorUri.setStatus("current")
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAction_Object = MibScalar
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAction = _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 4, 100),
    _Cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAction_Type()
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAction.setStatus("current")
_Cie1000IpmcSnoopingConfigMldGlobals_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingConfigMldGlobals = _Cie1000IpmcSnoopingConfigMldGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 5)
)
_Cie1000IpmcSnoopingConfigMldGlobalsAdminState_Type = TruthValue
_Cie1000IpmcSnoopingConfigMldGlobalsAdminState_Object = MibScalar
cie1000IpmcSnoopingConfigMldGlobalsAdminState = _Cie1000IpmcSnoopingConfigMldGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 5, 1),
    _Cie1000IpmcSnoopingConfigMldGlobalsAdminState_Type()
)
cie1000IpmcSnoopingConfigMldGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldGlobalsAdminState.setStatus("current")
_Cie1000IpmcSnoopingConfigMldGlobalsUnregisteredFlooding_Type = TruthValue
_Cie1000IpmcSnoopingConfigMldGlobalsUnregisteredFlooding_Object = MibScalar
cie1000IpmcSnoopingConfigMldGlobalsUnregisteredFlooding = _Cie1000IpmcSnoopingConfigMldGlobalsUnregisteredFlooding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 5, 2),
    _Cie1000IpmcSnoopingConfigMldGlobalsUnregisteredFlooding_Type()
)
cie1000IpmcSnoopingConfigMldGlobalsUnregisteredFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldGlobalsUnregisteredFlooding.setStatus("current")
_Cie1000IpmcSnoopingConfigMldGlobalsSsmRangeAddress_Type = InetAddressIPv6
_Cie1000IpmcSnoopingConfigMldGlobalsSsmRangeAddress_Object = MibScalar
cie1000IpmcSnoopingConfigMldGlobalsSsmRangeAddress = _Cie1000IpmcSnoopingConfigMldGlobalsSsmRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 5, 3),
    _Cie1000IpmcSnoopingConfigMldGlobalsSsmRangeAddress_Type()
)
cie1000IpmcSnoopingConfigMldGlobalsSsmRangeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldGlobalsSsmRangeAddress.setStatus("current")
_Cie1000IpmcSnoopingConfigMldGlobalsSsmRangeMask_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldGlobalsSsmRangeMask_Object = MibScalar
cie1000IpmcSnoopingConfigMldGlobalsSsmRangeMask = _Cie1000IpmcSnoopingConfigMldGlobalsSsmRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 5, 4),
    _Cie1000IpmcSnoopingConfigMldGlobalsSsmRangeMask_Type()
)
cie1000IpmcSnoopingConfigMldGlobalsSsmRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldGlobalsSsmRangeMask.setStatus("current")
_Cie1000IpmcSnoopingConfigMldGlobalsProxy_Type = TruthValue
_Cie1000IpmcSnoopingConfigMldGlobalsProxy_Object = MibScalar
cie1000IpmcSnoopingConfigMldGlobalsProxy = _Cie1000IpmcSnoopingConfigMldGlobalsProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 5, 5),
    _Cie1000IpmcSnoopingConfigMldGlobalsProxy_Type()
)
cie1000IpmcSnoopingConfigMldGlobalsProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldGlobalsProxy.setStatus("current")
_Cie1000IpmcSnoopingConfigMldGlobalsLeaveProxy_Type = TruthValue
_Cie1000IpmcSnoopingConfigMldGlobalsLeaveProxy_Object = MibScalar
cie1000IpmcSnoopingConfigMldGlobalsLeaveProxy = _Cie1000IpmcSnoopingConfigMldGlobalsLeaveProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 5, 6),
    _Cie1000IpmcSnoopingConfigMldGlobalsLeaveProxy_Type()
)
cie1000IpmcSnoopingConfigMldGlobalsLeaveProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldGlobalsLeaveProxy.setStatus("current")
_Cie1000IpmcSnoopingConfigMldPortTable_Object = MibTable
cie1000IpmcSnoopingConfigMldPortTable = _Cie1000IpmcSnoopingConfigMldPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldPortTable.setStatus("current")
_Cie1000IpmcSnoopingConfigMldPortEntry_Object = MibTableRow
cie1000IpmcSnoopingConfigMldPortEntry = _Cie1000IpmcSnoopingConfigMldPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 6, 1)
)
cie1000IpmcSnoopingConfigMldPortEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldPortPortIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldPortEntry.setStatus("current")
_Cie1000IpmcSnoopingConfigMldPortPortIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingConfigMldPortPortIndex_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldPortPortIndex = _Cie1000IpmcSnoopingConfigMldPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 6, 1, 1),
    _Cie1000IpmcSnoopingConfigMldPortPortIndex_Type()
)
cie1000IpmcSnoopingConfigMldPortPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldPortPortIndex.setStatus("current")
_Cie1000IpmcSnoopingConfigMldPortAsRouterPort_Type = TruthValue
_Cie1000IpmcSnoopingConfigMldPortAsRouterPort_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldPortAsRouterPort = _Cie1000IpmcSnoopingConfigMldPortAsRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 6, 1, 2),
    _Cie1000IpmcSnoopingConfigMldPortAsRouterPort_Type()
)
cie1000IpmcSnoopingConfigMldPortAsRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldPortAsRouterPort.setStatus("current")
_Cie1000IpmcSnoopingConfigMldPortDoFastLeave_Type = TruthValue
_Cie1000IpmcSnoopingConfigMldPortDoFastLeave_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldPortDoFastLeave = _Cie1000IpmcSnoopingConfigMldPortDoFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 6, 1, 3),
    _Cie1000IpmcSnoopingConfigMldPortDoFastLeave_Type()
)
cie1000IpmcSnoopingConfigMldPortDoFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldPortDoFastLeave.setStatus("current")
_Cie1000IpmcSnoopingConfigMldPortThrottlingNumber_Type = Integer32
_Cie1000IpmcSnoopingConfigMldPortThrottlingNumber_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldPortThrottlingNumber = _Cie1000IpmcSnoopingConfigMldPortThrottlingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 6, 1, 4),
    _Cie1000IpmcSnoopingConfigMldPortThrottlingNumber_Type()
)
cie1000IpmcSnoopingConfigMldPortThrottlingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldPortThrottlingNumber.setStatus("current")


class _Cie1000IpmcSnoopingConfigMldPortFilteringProfile_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcSnoopingConfigMldPortFilteringProfile based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcSnoopingConfigMldPortFilteringProfile_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcSnoopingConfigMldPortFilteringProfile_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldPortFilteringProfile = _Cie1000IpmcSnoopingConfigMldPortFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 6, 1, 5),
    _Cie1000IpmcSnoopingConfigMldPortFilteringProfile_Type()
)
cie1000IpmcSnoopingConfigMldPortFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldPortFilteringProfile.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTable_Object = MibTable
cie1000IpmcSnoopingConfigMldIfTable = _Cie1000IpmcSnoopingConfigMldIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTable.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfEntry_Object = MibTableRow
cie1000IpmcSnoopingConfigMldIfEntry = _Cie1000IpmcSnoopingConfigMldIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1)
)
cie1000IpmcSnoopingConfigMldIfEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfEntry.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingConfigMldIfIfIndex_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfIfIndex = _Cie1000IpmcSnoopingConfigMldIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 1),
    _Cie1000IpmcSnoopingConfigMldIfIfIndex_Type()
)
cie1000IpmcSnoopingConfigMldIfIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfIfIndex.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfAdminState_Type = TruthValue
_Cie1000IpmcSnoopingConfigMldIfAdminState_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfAdminState = _Cie1000IpmcSnoopingConfigMldIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 2),
    _Cie1000IpmcSnoopingConfigMldIfAdminState_Type()
)
cie1000IpmcSnoopingConfigMldIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfAdminState.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfQuerierElection_Type = TruthValue
_Cie1000IpmcSnoopingConfigMldIfQuerierElection_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfQuerierElection = _Cie1000IpmcSnoopingConfigMldIfQuerierElection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 3),
    _Cie1000IpmcSnoopingConfigMldIfQuerierElection_Type()
)
cie1000IpmcSnoopingConfigMldIfQuerierElection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfQuerierElection.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfCompatibility_Type = CIE1000IpmcSnoopingMldInterfaceCompatibilityEnum
_Cie1000IpmcSnoopingConfigMldIfCompatibility_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfCompatibility = _Cie1000IpmcSnoopingConfigMldIfCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 4),
    _Cie1000IpmcSnoopingConfigMldIfCompatibility_Type()
)
cie1000IpmcSnoopingConfigMldIfCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfCompatibility.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfPriority_Type = CIE1000Unsigned8
_Cie1000IpmcSnoopingConfigMldIfPriority_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfPriority = _Cie1000IpmcSnoopingConfigMldIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 5),
    _Cie1000IpmcSnoopingConfigMldIfPriority_Type()
)
cie1000IpmcSnoopingConfigMldIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfPriority.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfRv_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldIfRv_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfRv = _Cie1000IpmcSnoopingConfigMldIfRv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 6),
    _Cie1000IpmcSnoopingConfigMldIfRv_Type()
)
cie1000IpmcSnoopingConfigMldIfRv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfRv.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfQi_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldIfQi_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfQi = _Cie1000IpmcSnoopingConfigMldIfQi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 7),
    _Cie1000IpmcSnoopingConfigMldIfQi_Type()
)
cie1000IpmcSnoopingConfigMldIfQi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfQi.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfQri_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldIfQri_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfQri = _Cie1000IpmcSnoopingConfigMldIfQri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 8),
    _Cie1000IpmcSnoopingConfigMldIfQri_Type()
)
cie1000IpmcSnoopingConfigMldIfQri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfQri.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfLlqi_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldIfLlqi_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfLlqi = _Cie1000IpmcSnoopingConfigMldIfLlqi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 9),
    _Cie1000IpmcSnoopingConfigMldIfLlqi_Type()
)
cie1000IpmcSnoopingConfigMldIfLlqi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfLlqi.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfUri_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldIfUri_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfUri = _Cie1000IpmcSnoopingConfigMldIfUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 10),
    _Cie1000IpmcSnoopingConfigMldIfUri_Type()
)
cie1000IpmcSnoopingConfigMldIfUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfUri.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfAction_Type = CIE1000RowEditorState
_Cie1000IpmcSnoopingConfigMldIfAction_Object = MibTableColumn
cie1000IpmcSnoopingConfigMldIfAction = _Cie1000IpmcSnoopingConfigMldIfAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 7, 1, 100),
    _Cie1000IpmcSnoopingConfigMldIfAction_Type()
)
cie1000IpmcSnoopingConfigMldIfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfAction.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingConfigMldIfTableRowEditor = _Cie1000IpmcSnoopingConfigMldIfTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8)
)
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorIfIndex_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorIfIndex = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 1),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorIfIndex_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorIfIndex.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorAdminState_Type = TruthValue
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorAdminState_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorAdminState = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 2),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorAdminState_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorAdminState.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorQuerierElection_Type = TruthValue
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorQuerierElection_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorQuerierElection = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorQuerierElection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 3),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorQuerierElection_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorQuerierElection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorQuerierElection.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorCompatibility_Type = CIE1000IpmcSnoopingMldInterfaceCompatibilityEnum
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorCompatibility_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorCompatibility = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 4),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorCompatibility_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorCompatibility.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorPriority_Type = CIE1000Unsigned8
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorPriority_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorPriority = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 5),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorPriority_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorPriority.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorRv_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorRv_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorRv = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorRv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 6),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorRv_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorRv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorRv.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorQi_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorQi_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorQi = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorQi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 7),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorQi_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorQi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorQi.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorQri_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorQri_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorQri = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorQri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 8),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorQri_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorQri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorQri.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorLlqi_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorLlqi_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorLlqi = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorLlqi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 9),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorLlqi_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorLlqi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorLlqi.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorUri_Type = Unsigned32
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorUri_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorUri = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 10),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorUri_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorUri.setStatus("current")
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000IpmcSnoopingConfigMldIfTableRowEditorAction_Object = MibScalar
cie1000IpmcSnoopingConfigMldIfTableRowEditorAction = _Cie1000IpmcSnoopingConfigMldIfTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 2, 8, 100),
    _Cie1000IpmcSnoopingConfigMldIfTableRowEditorAction_Type()
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorAction.setStatus("current")
_Cie1000IpmcSnoopingStatus_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingStatus = _Cie1000IpmcSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3)
)
_Cie1000IpmcSnoopingStatusGroupAddressCount_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingStatusGroupAddressCount = _Cie1000IpmcSnoopingStatusGroupAddressCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 1)
)
_Cie1000IpmcSnoopingStatusGroupAddressCountFromIgmp_Type = Unsigned32
_Cie1000IpmcSnoopingStatusGroupAddressCountFromIgmp_Object = MibScalar
cie1000IpmcSnoopingStatusGroupAddressCountFromIgmp = _Cie1000IpmcSnoopingStatusGroupAddressCountFromIgmp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 1, 1),
    _Cie1000IpmcSnoopingStatusGroupAddressCountFromIgmp_Type()
)
cie1000IpmcSnoopingStatusGroupAddressCountFromIgmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusGroupAddressCountFromIgmp.setStatus("current")
_Cie1000IpmcSnoopingStatusGroupAddressCountFromMld_Type = Unsigned32
_Cie1000IpmcSnoopingStatusGroupAddressCountFromMld_Object = MibScalar
cie1000IpmcSnoopingStatusGroupAddressCountFromMld = _Cie1000IpmcSnoopingStatusGroupAddressCountFromMld_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 1, 2),
    _Cie1000IpmcSnoopingStatusGroupAddressCountFromMld_Type()
)
cie1000IpmcSnoopingStatusGroupAddressCountFromMld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusGroupAddressCountFromMld.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpRouterPortTable_Object = MibTable
cie1000IpmcSnoopingStatusIgmpRouterPortTable = _Cie1000IpmcSnoopingStatusIgmpRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpRouterPortTable.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpRouterPortEntry_Object = MibTableRow
cie1000IpmcSnoopingStatusIgmpRouterPortEntry = _Cie1000IpmcSnoopingStatusIgmpRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 2, 1)
)
cie1000IpmcSnoopingStatusIgmpRouterPortEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpRouterPortEntry.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex = _Cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 2, 1, 1),
    _Cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex_Type()
)
cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpRouterPortStatus_Type = CIE1000IpmcSnoopingIgmpRouterPortStatusEnum
_Cie1000IpmcSnoopingStatusIgmpRouterPortStatus_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpRouterPortStatus = _Cie1000IpmcSnoopingStatusIgmpRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 2, 1, 2),
    _Cie1000IpmcSnoopingStatusIgmpRouterPortStatus_Type()
)
cie1000IpmcSnoopingStatusIgmpRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpRouterPortStatus.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanTable_Object = MibTable
cie1000IpmcSnoopingStatusIgmpVlanTable = _Cie1000IpmcSnoopingStatusIgmpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanTable.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanEntry_Object = MibTableRow
cie1000IpmcSnoopingStatusIgmpVlanEntry = _Cie1000IpmcSnoopingStatusIgmpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1)
)
cie1000IpmcSnoopingStatusIgmpVlanEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanEntry.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingStatusIgmpVlanIfIndex_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanIfIndex = _Cie1000IpmcSnoopingStatusIgmpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 1),
    _Cie1000IpmcSnoopingStatusIgmpVlanIfIndex_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanIfIndex.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanQuerierStatus_Type = CIE1000IpmcSnoopingIgmpVlanStatusQuerierStatusEnum
_Cie1000IpmcSnoopingStatusIgmpVlanQuerierStatus_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanQuerierStatus = _Cie1000IpmcSnoopingStatusIgmpVlanQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 2),
    _Cie1000IpmcSnoopingStatusIgmpVlanQuerierStatus_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanQuerierStatus.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanActiveQuerierAddress_Type = IpAddress
_Cie1000IpmcSnoopingStatusIgmpVlanActiveQuerierAddress_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanActiveQuerierAddress = _Cie1000IpmcSnoopingStatusIgmpVlanActiveQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 3),
    _Cie1000IpmcSnoopingStatusIgmpVlanActiveQuerierAddress_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanActiveQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanActiveQuerierAddress.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanQuerierUptime_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanQuerierUptime_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanQuerierUptime = _Cie1000IpmcSnoopingStatusIgmpVlanQuerierUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 4),
    _Cie1000IpmcSnoopingStatusIgmpVlanQuerierUptime_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanQuerierUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanQuerierUptime.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanQueryInterval_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanQueryInterval_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanQueryInterval = _Cie1000IpmcSnoopingStatusIgmpVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 5),
    _Cie1000IpmcSnoopingStatusIgmpVlanQueryInterval_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanQueryInterval.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanStartupQueryCount_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanStartupQueryCount_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanStartupQueryCount = _Cie1000IpmcSnoopingStatusIgmpVlanStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 6),
    _Cie1000IpmcSnoopingStatusIgmpVlanStartupQueryCount_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanStartupQueryCount.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanQuerierExpiryTime_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanQuerierExpiryTime_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanQuerierExpiryTime = _Cie1000IpmcSnoopingStatusIgmpVlanQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 7),
    _Cie1000IpmcSnoopingStatusIgmpVlanQuerierExpiryTime_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanQuerierExpiryTime.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanQuerierVersion_Type = CIE1000Unsigned8
_Cie1000IpmcSnoopingStatusIgmpVlanQuerierVersion_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanQuerierVersion = _Cie1000IpmcSnoopingStatusIgmpVlanQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 8),
    _Cie1000IpmcSnoopingStatusIgmpVlanQuerierVersion_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanQuerierVersion.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanQuerierPresentTimeout_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanQuerierPresentTimeout_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanQuerierPresentTimeout = _Cie1000IpmcSnoopingStatusIgmpVlanQuerierPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 9),
    _Cie1000IpmcSnoopingStatusIgmpVlanQuerierPresentTimeout_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanQuerierPresentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanQuerierPresentTimeout.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanHostVersion_Type = CIE1000Unsigned8
_Cie1000IpmcSnoopingStatusIgmpVlanHostVersion_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanHostVersion = _Cie1000IpmcSnoopingStatusIgmpVlanHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 10),
    _Cie1000IpmcSnoopingStatusIgmpVlanHostVersion_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanHostVersion.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanHostPresentTimeout_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanHostPresentTimeout_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanHostPresentTimeout = _Cie1000IpmcSnoopingStatusIgmpVlanHostPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 11),
    _Cie1000IpmcSnoopingStatusIgmpVlanHostPresentTimeout_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanHostPresentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanHostPresentTimeout.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanCounterTxQuery_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanCounterTxQuery_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanCounterTxQuery = _Cie1000IpmcSnoopingStatusIgmpVlanCounterTxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 12),
    _Cie1000IpmcSnoopingStatusIgmpVlanCounterTxQuery_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanCounterTxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanCounterTxQuery.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanCounterTxSpecificQuery_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanCounterTxSpecificQuery_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanCounterTxSpecificQuery = _Cie1000IpmcSnoopingStatusIgmpVlanCounterTxSpecificQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 13),
    _Cie1000IpmcSnoopingStatusIgmpVlanCounterTxSpecificQuery_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanCounterTxSpecificQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanCounterTxSpecificQuery.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxQuery_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxQuery_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanCounterRxQuery = _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 14),
    _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxQuery_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanCounterRxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanCounterRxQuery.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV1Join_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV1Join_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanCounterRxV1Join = _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV1Join_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 15),
    _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV1Join_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanCounterRxV1Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanCounterRxV1Join.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Join_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Join_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Join = _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Join_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 16),
    _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Join_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Join.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Leave_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Leave_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Leave = _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Leave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 17),
    _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Leave_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Leave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Leave.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV3Join_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV3Join_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanCounterRxV3Join = _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV3Join_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 18),
    _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxV3Join_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanCounterRxV3Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanCounterRxV3Join.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxErrors_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpVlanCounterRxErrors_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpVlanCounterRxErrors = _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 3, 1, 19),
    _Cie1000IpmcSnoopingStatusIgmpVlanCounterRxErrors_Type()
)
cie1000IpmcSnoopingStatusIgmpVlanCounterRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanCounterRxErrors.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupAddressTable_Object = MibTable
cie1000IpmcSnoopingStatusIgmpGroupAddressTable = _Cie1000IpmcSnoopingStatusIgmpGroupAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupAddressTable.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupAddressEntry_Object = MibTableRow
cie1000IpmcSnoopingStatusIgmpGroupAddressEntry = _Cie1000IpmcSnoopingStatusIgmpGroupAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 4, 1)
)
cie1000IpmcSnoopingStatusIgmpGroupAddressEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex"),
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupAddressEntry.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex = _Cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 4, 1, 1),
    _Cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress_Type = IpAddress
_Cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress = _Cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 4, 1, 2),
    _Cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupAddressMemberPorts_Type = CIE1000PortList
_Cie1000IpmcSnoopingStatusIgmpGroupAddressMemberPorts_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupAddressMemberPorts = _Cie1000IpmcSnoopingStatusIgmpGroupAddressMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 4, 1, 3),
    _Cie1000IpmcSnoopingStatusIgmpGroupAddressMemberPorts_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupAddressMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupAddressMemberPorts.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupAddressHardwareSwitch_Type = TruthValue
_Cie1000IpmcSnoopingStatusIgmpGroupAddressHardwareSwitch_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupAddressHardwareSwitch = _Cie1000IpmcSnoopingStatusIgmpGroupAddressHardwareSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 4, 1, 4),
    _Cie1000IpmcSnoopingStatusIgmpGroupAddressHardwareSwitch_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupAddressHardwareSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupAddressHardwareSwitch.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListTable_Object = MibTable
cie1000IpmcSnoopingStatusIgmpGroupSrcListTable = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListTable.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListEntry_Object = MibTableRow
cie1000IpmcSnoopingStatusIgmpGroupSrcListEntry = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5, 1)
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex"),
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress"),
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex"),
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListEntry.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5, 1, 1),
    _Cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress_Type = IpAddress
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5, 1, 2),
    _Cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5, 1, 3),
    _Cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress_Type = IpAddress
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5, 1, 4),
    _Cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupFilterMode_Type = CIE1000IpmcSnoopingIgmpGroupSrcListGroupFilterModeEnum
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupFilterMode_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupFilterMode = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5, 1, 5),
    _Cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupFilterMode_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupFilterMode.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListFilterTimer_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListFilterTimer_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupSrcListFilterTimer = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListFilterTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5, 1, 6),
    _Cie1000IpmcSnoopingStatusIgmpGroupSrcListFilterTimer_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListFilterTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListFilterTimer.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceType_Type = CIE1000IpmcSnoopingIgmpGroupSrcListSourceTypeEnum
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceType_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceType = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5, 1, 7),
    _Cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceType_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceType.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceTimer_Type = Unsigned32
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceTimer_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceTimer = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5, 1, 8),
    _Cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceTimer_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceTimer.setStatus("current")
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListHardwareFilter_Type = TruthValue
_Cie1000IpmcSnoopingStatusIgmpGroupSrcListHardwareFilter_Object = MibTableColumn
cie1000IpmcSnoopingStatusIgmpGroupSrcListHardwareFilter = _Cie1000IpmcSnoopingStatusIgmpGroupSrcListHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 5, 1, 9),
    _Cie1000IpmcSnoopingStatusIgmpGroupSrcListHardwareFilter_Type()
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListHardwareFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListHardwareFilter.setStatus("current")
_Cie1000IpmcSnoopingStatusMldRouterPortTable_Object = MibTable
cie1000IpmcSnoopingStatusMldRouterPortTable = _Cie1000IpmcSnoopingStatusMldRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldRouterPortTable.setStatus("current")
_Cie1000IpmcSnoopingStatusMldRouterPortEntry_Object = MibTableRow
cie1000IpmcSnoopingStatusMldRouterPortEntry = _Cie1000IpmcSnoopingStatusMldRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 6, 1)
)
cie1000IpmcSnoopingStatusMldRouterPortEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldRouterPortPortIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldRouterPortEntry.setStatus("current")
_Cie1000IpmcSnoopingStatusMldRouterPortPortIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingStatusMldRouterPortPortIndex_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldRouterPortPortIndex = _Cie1000IpmcSnoopingStatusMldRouterPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 6, 1, 1),
    _Cie1000IpmcSnoopingStatusMldRouterPortPortIndex_Type()
)
cie1000IpmcSnoopingStatusMldRouterPortPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldRouterPortPortIndex.setStatus("current")
_Cie1000IpmcSnoopingStatusMldRouterPortStatus_Type = CIE1000IpmcSnoopingMldRouterPortStatusEnum
_Cie1000IpmcSnoopingStatusMldRouterPortStatus_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldRouterPortStatus = _Cie1000IpmcSnoopingStatusMldRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 6, 1, 2),
    _Cie1000IpmcSnoopingStatusMldRouterPortStatus_Type()
)
cie1000IpmcSnoopingStatusMldRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldRouterPortStatus.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanTable_Object = MibTable
cie1000IpmcSnoopingStatusMldVlanTable = _Cie1000IpmcSnoopingStatusMldVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanTable.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanEntry_Object = MibTableRow
cie1000IpmcSnoopingStatusMldVlanEntry = _Cie1000IpmcSnoopingStatusMldVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1)
)
cie1000IpmcSnoopingStatusMldVlanEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanEntry.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingStatusMldVlanIfIndex_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanIfIndex = _Cie1000IpmcSnoopingStatusMldVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 1),
    _Cie1000IpmcSnoopingStatusMldVlanIfIndex_Type()
)
cie1000IpmcSnoopingStatusMldVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanIfIndex.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanQuerierStatus_Type = CIE1000IpmcSnoopingMldVlanStatusQuerierStatusEnum
_Cie1000IpmcSnoopingStatusMldVlanQuerierStatus_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanQuerierStatus = _Cie1000IpmcSnoopingStatusMldVlanQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 2),
    _Cie1000IpmcSnoopingStatusMldVlanQuerierStatus_Type()
)
cie1000IpmcSnoopingStatusMldVlanQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanQuerierStatus.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanActiveQuerierAddress_Type = InetAddressIPv6
_Cie1000IpmcSnoopingStatusMldVlanActiveQuerierAddress_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanActiveQuerierAddress = _Cie1000IpmcSnoopingStatusMldVlanActiveQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 3),
    _Cie1000IpmcSnoopingStatusMldVlanActiveQuerierAddress_Type()
)
cie1000IpmcSnoopingStatusMldVlanActiveQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanActiveQuerierAddress.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanQuerierUptime_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanQuerierUptime_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanQuerierUptime = _Cie1000IpmcSnoopingStatusMldVlanQuerierUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 4),
    _Cie1000IpmcSnoopingStatusMldVlanQuerierUptime_Type()
)
cie1000IpmcSnoopingStatusMldVlanQuerierUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanQuerierUptime.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanQueryInterval_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanQueryInterval_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanQueryInterval = _Cie1000IpmcSnoopingStatusMldVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 5),
    _Cie1000IpmcSnoopingStatusMldVlanQueryInterval_Type()
)
cie1000IpmcSnoopingStatusMldVlanQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanQueryInterval.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanStartupQueryCount_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanStartupQueryCount_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanStartupQueryCount = _Cie1000IpmcSnoopingStatusMldVlanStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 6),
    _Cie1000IpmcSnoopingStatusMldVlanStartupQueryCount_Type()
)
cie1000IpmcSnoopingStatusMldVlanStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanStartupQueryCount.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanQuerierExpiryTime_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanQuerierExpiryTime_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanQuerierExpiryTime = _Cie1000IpmcSnoopingStatusMldVlanQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 7),
    _Cie1000IpmcSnoopingStatusMldVlanQuerierExpiryTime_Type()
)
cie1000IpmcSnoopingStatusMldVlanQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanQuerierExpiryTime.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanQuerierVersion_Type = CIE1000Unsigned8
_Cie1000IpmcSnoopingStatusMldVlanQuerierVersion_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanQuerierVersion = _Cie1000IpmcSnoopingStatusMldVlanQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 8),
    _Cie1000IpmcSnoopingStatusMldVlanQuerierVersion_Type()
)
cie1000IpmcSnoopingStatusMldVlanQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanQuerierVersion.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanQuerierPresentTimeout_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanQuerierPresentTimeout_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanQuerierPresentTimeout = _Cie1000IpmcSnoopingStatusMldVlanQuerierPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 9),
    _Cie1000IpmcSnoopingStatusMldVlanQuerierPresentTimeout_Type()
)
cie1000IpmcSnoopingStatusMldVlanQuerierPresentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanQuerierPresentTimeout.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanHostVersion_Type = CIE1000Unsigned8
_Cie1000IpmcSnoopingStatusMldVlanHostVersion_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanHostVersion = _Cie1000IpmcSnoopingStatusMldVlanHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 10),
    _Cie1000IpmcSnoopingStatusMldVlanHostVersion_Type()
)
cie1000IpmcSnoopingStatusMldVlanHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanHostVersion.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanHostPresentTimeout_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanHostPresentTimeout_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanHostPresentTimeout = _Cie1000IpmcSnoopingStatusMldVlanHostPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 11),
    _Cie1000IpmcSnoopingStatusMldVlanHostPresentTimeout_Type()
)
cie1000IpmcSnoopingStatusMldVlanHostPresentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanHostPresentTimeout.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanCounterTxQuery_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanCounterTxQuery_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanCounterTxQuery = _Cie1000IpmcSnoopingStatusMldVlanCounterTxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 12),
    _Cie1000IpmcSnoopingStatusMldVlanCounterTxQuery_Type()
)
cie1000IpmcSnoopingStatusMldVlanCounterTxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanCounterTxQuery.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanCounterTxSpecificQuery_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanCounterTxSpecificQuery_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanCounterTxSpecificQuery = _Cie1000IpmcSnoopingStatusMldVlanCounterTxSpecificQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 13),
    _Cie1000IpmcSnoopingStatusMldVlanCounterTxSpecificQuery_Type()
)
cie1000IpmcSnoopingStatusMldVlanCounterTxSpecificQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanCounterTxSpecificQuery.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanCounterRxQuery_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanCounterRxQuery_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanCounterRxQuery = _Cie1000IpmcSnoopingStatusMldVlanCounterRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 14),
    _Cie1000IpmcSnoopingStatusMldVlanCounterRxQuery_Type()
)
cie1000IpmcSnoopingStatusMldVlanCounterRxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanCounterRxQuery.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanCounterRxV1Report_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanCounterRxV1Report_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanCounterRxV1Report = _Cie1000IpmcSnoopingStatusMldVlanCounterRxV1Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 15),
    _Cie1000IpmcSnoopingStatusMldVlanCounterRxV1Report_Type()
)
cie1000IpmcSnoopingStatusMldVlanCounterRxV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanCounterRxV1Report.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanCounterRxV1Done_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanCounterRxV1Done_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanCounterRxV1Done = _Cie1000IpmcSnoopingStatusMldVlanCounterRxV1Done_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 16),
    _Cie1000IpmcSnoopingStatusMldVlanCounterRxV1Done_Type()
)
cie1000IpmcSnoopingStatusMldVlanCounterRxV1Done.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanCounterRxV1Done.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanCounterRxV2Report_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanCounterRxV2Report_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanCounterRxV2Report = _Cie1000IpmcSnoopingStatusMldVlanCounterRxV2Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 17),
    _Cie1000IpmcSnoopingStatusMldVlanCounterRxV2Report_Type()
)
cie1000IpmcSnoopingStatusMldVlanCounterRxV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanCounterRxV2Report.setStatus("current")
_Cie1000IpmcSnoopingStatusMldVlanCounterRxErrors_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldVlanCounterRxErrors_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldVlanCounterRxErrors = _Cie1000IpmcSnoopingStatusMldVlanCounterRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 7, 1, 18),
    _Cie1000IpmcSnoopingStatusMldVlanCounterRxErrors_Type()
)
cie1000IpmcSnoopingStatusMldVlanCounterRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanCounterRxErrors.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupAddressTable_Object = MibTable
cie1000IpmcSnoopingStatusMldGroupAddressTable = _Cie1000IpmcSnoopingStatusMldGroupAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupAddressTable.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupAddressEntry_Object = MibTableRow
cie1000IpmcSnoopingStatusMldGroupAddressEntry = _Cie1000IpmcSnoopingStatusMldGroupAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 8, 1)
)
cie1000IpmcSnoopingStatusMldGroupAddressEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupAddressIfIndex"),
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupAddressEntry.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupAddressIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingStatusMldGroupAddressIfIndex_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupAddressIfIndex = _Cie1000IpmcSnoopingStatusMldGroupAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 8, 1, 1),
    _Cie1000IpmcSnoopingStatusMldGroupAddressIfIndex_Type()
)
cie1000IpmcSnoopingStatusMldGroupAddressIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupAddressIfIndex.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress_Type = InetAddressIPv6
_Cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress = _Cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 8, 1, 2),
    _Cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress_Type()
)
cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupAddressMemberPorts_Type = CIE1000PortList
_Cie1000IpmcSnoopingStatusMldGroupAddressMemberPorts_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupAddressMemberPorts = _Cie1000IpmcSnoopingStatusMldGroupAddressMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 8, 1, 3),
    _Cie1000IpmcSnoopingStatusMldGroupAddressMemberPorts_Type()
)
cie1000IpmcSnoopingStatusMldGroupAddressMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupAddressMemberPorts.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupAddressHardwareSwitch_Type = TruthValue
_Cie1000IpmcSnoopingStatusMldGroupAddressHardwareSwitch_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupAddressHardwareSwitch = _Cie1000IpmcSnoopingStatusMldGroupAddressHardwareSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 8, 1, 4),
    _Cie1000IpmcSnoopingStatusMldGroupAddressHardwareSwitch_Type()
)
cie1000IpmcSnoopingStatusMldGroupAddressHardwareSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupAddressHardwareSwitch.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListTable_Object = MibTable
cie1000IpmcSnoopingStatusMldGroupSrcListTable = _Cie1000IpmcSnoopingStatusMldGroupSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9)
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListTable.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListEntry_Object = MibTableRow
cie1000IpmcSnoopingStatusMldGroupSrcListEntry = _Cie1000IpmcSnoopingStatusMldGroupSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9, 1)
)
cie1000IpmcSnoopingStatusMldGroupSrcListEntry.setIndexNames(
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex"),
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress"),
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex"),
    (0, "CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListEntry.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex = _Cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9, 1, 1),
    _Cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex_Type()
)
cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress_Type = InetAddressIPv6
_Cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress = _Cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9, 1, 2),
    _Cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress_Type()
)
cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex = _Cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9, 1, 3),
    _Cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex_Type()
)
cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress_Type = InetAddressIPv6
_Cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress = _Cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9, 1, 4),
    _Cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress_Type()
)
cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListGroupFilterMode_Type = CIE1000IpmcSnoopingMldGroupSrcListGroupFilterModeEnum
_Cie1000IpmcSnoopingStatusMldGroupSrcListGroupFilterMode_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupSrcListGroupFilterMode = _Cie1000IpmcSnoopingStatusMldGroupSrcListGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9, 1, 5),
    _Cie1000IpmcSnoopingStatusMldGroupSrcListGroupFilterMode_Type()
)
cie1000IpmcSnoopingStatusMldGroupSrcListGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListGroupFilterMode.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListFilterTimer_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldGroupSrcListFilterTimer_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupSrcListFilterTimer = _Cie1000IpmcSnoopingStatusMldGroupSrcListFilterTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9, 1, 6),
    _Cie1000IpmcSnoopingStatusMldGroupSrcListFilterTimer_Type()
)
cie1000IpmcSnoopingStatusMldGroupSrcListFilterTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListFilterTimer.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListSourceType_Type = CIE1000IpmcSnoopingMldGroupSrcListSourceEnum
_Cie1000IpmcSnoopingStatusMldGroupSrcListSourceType_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupSrcListSourceType = _Cie1000IpmcSnoopingStatusMldGroupSrcListSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9, 1, 7),
    _Cie1000IpmcSnoopingStatusMldGroupSrcListSourceType_Type()
)
cie1000IpmcSnoopingStatusMldGroupSrcListSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListSourceType.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListSourceTimer_Type = Unsigned32
_Cie1000IpmcSnoopingStatusMldGroupSrcListSourceTimer_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupSrcListSourceTimer = _Cie1000IpmcSnoopingStatusMldGroupSrcListSourceTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9, 1, 8),
    _Cie1000IpmcSnoopingStatusMldGroupSrcListSourceTimer_Type()
)
cie1000IpmcSnoopingStatusMldGroupSrcListSourceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListSourceTimer.setStatus("current")
_Cie1000IpmcSnoopingStatusMldGroupSrcListHardwareFilter_Type = TruthValue
_Cie1000IpmcSnoopingStatusMldGroupSrcListHardwareFilter_Object = MibTableColumn
cie1000IpmcSnoopingStatusMldGroupSrcListHardwareFilter = _Cie1000IpmcSnoopingStatusMldGroupSrcListHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 3, 9, 1, 9),
    _Cie1000IpmcSnoopingStatusMldGroupSrcListHardwareFilter_Type()
)
cie1000IpmcSnoopingStatusMldGroupSrcListHardwareFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListHardwareFilter.setStatus("current")
_Cie1000IpmcSnoopingControl_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingControl = _Cie1000IpmcSnoopingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 4)
)
_Cie1000IpmcSnoopingControlStatistics_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingControlStatistics = _Cie1000IpmcSnoopingControlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 4, 1)
)
_Cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndex_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndex = _Cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 4, 1, 1)
)
_Cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex_Object = MibScalar
cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex = _Cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 4, 1, 1, 1),
    _Cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex_Type()
)
cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex.setStatus("current")
_Cie1000IpmcSnoopingControlStatisticsMldClearByIfIndex_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingControlStatisticsMldClearByIfIndex = _Cie1000IpmcSnoopingControlStatisticsMldClearByIfIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 4, 1, 2)
)
_Cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex_Object = MibScalar
cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex = _Cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 1, 4, 1, 2, 1),
    _Cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex_Type()
)
cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex.setStatus("current")
_Cie1000IpmcSnoopingMibConformance_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingMibConformance = _Cie1000IpmcSnoopingMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2)
)
_Cie1000IpmcSnoopingMibCompliances_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingMibCompliances = _Cie1000IpmcSnoopingMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 1)
)
_Cie1000IpmcSnoopingMibGroups_ObjectIdentity = ObjectIdentity
cie1000IpmcSnoopingMibGroups = _Cie1000IpmcSnoopingMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2)
)

# Managed Objects groups

cie1000IpmcSnoopingConfigIgmpGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 1)
)
cie1000IpmcSnoopingConfigIgmpGlobalsInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpGlobalsAdminState"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpGlobalsUnregisteredFlooding"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeMask"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpGlobalsProxy"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpGlobalsLeaveProxy"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpGlobalsInfoGroup.setStatus("current")

cie1000IpmcSnoopingConfigIgmpPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 2)
)
cie1000IpmcSnoopingConfigIgmpPortTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpPortPortIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpPortAsRouterPort"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpPortDoFastLeave"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpPortThrottlingNumber"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpPortFilteringProfile"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpPortTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingConfigIgmpIfTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 3)
)
cie1000IpmcSnoopingConfigIgmpIfTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfIfIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfAdminState"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfQuerierElection"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfQuerierAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfCompatibility"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfPriority"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfRv"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfQi"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfQri"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfLmqi"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfUri"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingConfigIgmpIfTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 4)
)
cie1000IpmcSnoopingConfigIgmpIfTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorIfIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAdminState"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierElection"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorCompatibility"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorPriority"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorRv"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQi"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQri"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorLmqi"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorUri"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigIgmpIfTableRowEditorInfoGroup.setStatus("current")

cie1000IpmcSnoopingConfigMldGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 5)
)
cie1000IpmcSnoopingConfigMldGlobalsInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldGlobalsAdminState"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldGlobalsUnregisteredFlooding"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldGlobalsSsmRangeAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldGlobalsSsmRangeMask"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldGlobalsProxy"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldGlobalsLeaveProxy"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldGlobalsInfoGroup.setStatus("current")

cie1000IpmcSnoopingConfigMldPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 6)
)
cie1000IpmcSnoopingConfigMldPortTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldPortPortIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldPortAsRouterPort"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldPortDoFastLeave"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldPortThrottlingNumber"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldPortFilteringProfile"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldPortTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingConfigMldIfTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 7)
)
cie1000IpmcSnoopingConfigMldIfTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfIfIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfAdminState"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfQuerierElection"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfCompatibility"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfPriority"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfRv"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfQi"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfQri"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfLlqi"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfUri"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingConfigMldIfTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 8)
)
cie1000IpmcSnoopingConfigMldIfTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorIfIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorAdminState"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorQuerierElection"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorCompatibility"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorPriority"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorRv"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorQi"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorQri"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorLlqi"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorUri"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingConfigMldIfTableRowEditorInfoGroup.setStatus("current")

cie1000IpmcSnoopingStatusGroupAddressCountInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 9)
)
cie1000IpmcSnoopingStatusGroupAddressCountInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusGroupAddressCountFromIgmp"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusGroupAddressCountFromMld"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusGroupAddressCountInfoGroup.setStatus("current")

cie1000IpmcSnoopingStatusIgmpRouterPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 10)
)
cie1000IpmcSnoopingStatusIgmpRouterPortTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpRouterPortStatus"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpRouterPortTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingStatusIgmpVlanTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 11)
)
cie1000IpmcSnoopingStatusIgmpVlanTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanIfIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanQuerierStatus"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanActiveQuerierAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanQuerierUptime"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanQueryInterval"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanStartupQueryCount"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanQuerierExpiryTime"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanQuerierVersion"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanQuerierPresentTimeout"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanHostVersion"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanHostPresentTimeout"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanCounterTxQuery"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanCounterTxSpecificQuery"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanCounterRxQuery"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanCounterRxV1Join"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Join"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Leave"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanCounterRxV3Join"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanCounterRxErrors"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpVlanTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingStatusIgmpGroupAddressTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 12)
)
cie1000IpmcSnoopingStatusIgmpGroupAddressTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupAddressMemberPorts"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupAddressHardwareSwitch"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupAddressTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingStatusIgmpGroupSrcListTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 13)
)
cie1000IpmcSnoopingStatusIgmpGroupSrcListTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupFilterMode"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListFilterTimer"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceType"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceTimer"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListHardwareFilter"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusIgmpGroupSrcListTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingStatusMldRouterPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 14)
)
cie1000IpmcSnoopingStatusMldRouterPortTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldRouterPortPortIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldRouterPortStatus"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldRouterPortTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingStatusMldVlanTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 15)
)
cie1000IpmcSnoopingStatusMldVlanTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanIfIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanQuerierStatus"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanActiveQuerierAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanQuerierUptime"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanQueryInterval"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanStartupQueryCount"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanQuerierExpiryTime"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanQuerierVersion"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanQuerierPresentTimeout"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanHostVersion"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanHostPresentTimeout"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanCounterTxQuery"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanCounterTxSpecificQuery"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanCounterRxQuery"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanCounterRxV1Report"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanCounterRxV1Done"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanCounterRxV2Report"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanCounterRxErrors"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldVlanTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingStatusMldGroupAddressTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 16)
)
cie1000IpmcSnoopingStatusMldGroupAddressTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupAddressIfIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupAddressMemberPorts"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupAddressHardwareSwitch"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupAddressTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingStatusMldGroupSrcListTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 17)
)
cie1000IpmcSnoopingStatusMldGroupSrcListTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListGroupFilterMode"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListFilterTimer"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListSourceType"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListSourceTimer"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListHardwareFilter"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingStatusMldGroupSrcListTableInfoGroup.setStatus("current")

cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 18)
)
cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup.setObjects(
    ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex")
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup.setStatus("current")

cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 2, 19)
)
cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup.setObjects(
    ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex")
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000IpmcSnoopingMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 69, 2, 1, 1)
)
cie1000IpmcSnoopingMibCompliance.setObjects(
      *(("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpGlobalsInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpPortTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldGlobalsInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldPortTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingConfigMldIfTableRowEditorInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusGroupAddressCountInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpRouterPortTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpVlanTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupAddressTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusIgmpGroupSrcListTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldRouterPortTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldVlanTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupAddressTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingStatusMldGroupSrcListTableInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup"),
        ("CIE1000-IPMC-SNOOPING-MIB", "cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000IpmcSnoopingMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-IPMC-SNOOPING-MIB",
    **{"CIE1000IpmcSnoopingIgmpGroupSrcListGroupFilterModeEnum": CIE1000IpmcSnoopingIgmpGroupSrcListGroupFilterModeEnum,
       "CIE1000IpmcSnoopingIgmpGroupSrcListSourceTypeEnum": CIE1000IpmcSnoopingIgmpGroupSrcListSourceTypeEnum,
       "CIE1000IpmcSnoopingIgmpInterfaceCompatibilityEnum": CIE1000IpmcSnoopingIgmpInterfaceCompatibilityEnum,
       "CIE1000IpmcSnoopingIgmpRouterPortStatusEnum": CIE1000IpmcSnoopingIgmpRouterPortStatusEnum,
       "CIE1000IpmcSnoopingIgmpVlanStatusQuerierStatusEnum": CIE1000IpmcSnoopingIgmpVlanStatusQuerierStatusEnum,
       "CIE1000IpmcSnoopingMldGroupSrcListGroupFilterModeEnum": CIE1000IpmcSnoopingMldGroupSrcListGroupFilterModeEnum,
       "CIE1000IpmcSnoopingMldGroupSrcListSourceEnum": CIE1000IpmcSnoopingMldGroupSrcListSourceEnum,
       "CIE1000IpmcSnoopingMldInterfaceCompatibilityEnum": CIE1000IpmcSnoopingMldInterfaceCompatibilityEnum,
       "CIE1000IpmcSnoopingMldRouterPortStatusEnum": CIE1000IpmcSnoopingMldRouterPortStatusEnum,
       "CIE1000IpmcSnoopingMldVlanStatusQuerierStatusEnum": CIE1000IpmcSnoopingMldVlanStatusQuerierStatusEnum,
       "cie1000IpmcSnoopingMib": cie1000IpmcSnoopingMib,
       "cie1000IpmcSnoopingMibObjects": cie1000IpmcSnoopingMibObjects,
       "cie1000IpmcSnoopingConfig": cie1000IpmcSnoopingConfig,
       "cie1000IpmcSnoopingConfigIgmpGlobals": cie1000IpmcSnoopingConfigIgmpGlobals,
       "cie1000IpmcSnoopingConfigIgmpGlobalsAdminState": cie1000IpmcSnoopingConfigIgmpGlobalsAdminState,
       "cie1000IpmcSnoopingConfigIgmpGlobalsUnregisteredFlooding": cie1000IpmcSnoopingConfigIgmpGlobalsUnregisteredFlooding,
       "cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeAddress": cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeAddress,
       "cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeMask": cie1000IpmcSnoopingConfigIgmpGlobalsSsmRangeMask,
       "cie1000IpmcSnoopingConfigIgmpGlobalsProxy": cie1000IpmcSnoopingConfigIgmpGlobalsProxy,
       "cie1000IpmcSnoopingConfigIgmpGlobalsLeaveProxy": cie1000IpmcSnoopingConfigIgmpGlobalsLeaveProxy,
       "cie1000IpmcSnoopingConfigIgmpPortTable": cie1000IpmcSnoopingConfigIgmpPortTable,
       "cie1000IpmcSnoopingConfigIgmpPortEntry": cie1000IpmcSnoopingConfigIgmpPortEntry,
       "cie1000IpmcSnoopingConfigIgmpPortPortIndex": cie1000IpmcSnoopingConfigIgmpPortPortIndex,
       "cie1000IpmcSnoopingConfigIgmpPortAsRouterPort": cie1000IpmcSnoopingConfigIgmpPortAsRouterPort,
       "cie1000IpmcSnoopingConfigIgmpPortDoFastLeave": cie1000IpmcSnoopingConfigIgmpPortDoFastLeave,
       "cie1000IpmcSnoopingConfigIgmpPortThrottlingNumber": cie1000IpmcSnoopingConfigIgmpPortThrottlingNumber,
       "cie1000IpmcSnoopingConfigIgmpPortFilteringProfile": cie1000IpmcSnoopingConfigIgmpPortFilteringProfile,
       "cie1000IpmcSnoopingConfigIgmpIfTable": cie1000IpmcSnoopingConfigIgmpIfTable,
       "cie1000IpmcSnoopingConfigIgmpIfEntry": cie1000IpmcSnoopingConfigIgmpIfEntry,
       "cie1000IpmcSnoopingConfigIgmpIfIfIndex": cie1000IpmcSnoopingConfigIgmpIfIfIndex,
       "cie1000IpmcSnoopingConfigIgmpIfAdminState": cie1000IpmcSnoopingConfigIgmpIfAdminState,
       "cie1000IpmcSnoopingConfigIgmpIfQuerierElection": cie1000IpmcSnoopingConfigIgmpIfQuerierElection,
       "cie1000IpmcSnoopingConfigIgmpIfQuerierAddress": cie1000IpmcSnoopingConfigIgmpIfQuerierAddress,
       "cie1000IpmcSnoopingConfigIgmpIfCompatibility": cie1000IpmcSnoopingConfigIgmpIfCompatibility,
       "cie1000IpmcSnoopingConfigIgmpIfPriority": cie1000IpmcSnoopingConfigIgmpIfPriority,
       "cie1000IpmcSnoopingConfigIgmpIfRv": cie1000IpmcSnoopingConfigIgmpIfRv,
       "cie1000IpmcSnoopingConfigIgmpIfQi": cie1000IpmcSnoopingConfigIgmpIfQi,
       "cie1000IpmcSnoopingConfigIgmpIfQri": cie1000IpmcSnoopingConfigIgmpIfQri,
       "cie1000IpmcSnoopingConfigIgmpIfLmqi": cie1000IpmcSnoopingConfigIgmpIfLmqi,
       "cie1000IpmcSnoopingConfigIgmpIfUri": cie1000IpmcSnoopingConfigIgmpIfUri,
       "cie1000IpmcSnoopingConfigIgmpIfAction": cie1000IpmcSnoopingConfigIgmpIfAction,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditor": cie1000IpmcSnoopingConfigIgmpIfTableRowEditor,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorIfIndex": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorIfIndex,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAdminState": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAdminState,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierElection": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierElection,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierAddress": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQuerierAddress,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorCompatibility": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorCompatibility,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorPriority": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorPriority,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorRv": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorRv,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQi": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQi,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQri": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorQri,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorLmqi": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorLmqi,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorUri": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorUri,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAction": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorAction,
       "cie1000IpmcSnoopingConfigMldGlobals": cie1000IpmcSnoopingConfigMldGlobals,
       "cie1000IpmcSnoopingConfigMldGlobalsAdminState": cie1000IpmcSnoopingConfigMldGlobalsAdminState,
       "cie1000IpmcSnoopingConfigMldGlobalsUnregisteredFlooding": cie1000IpmcSnoopingConfigMldGlobalsUnregisteredFlooding,
       "cie1000IpmcSnoopingConfigMldGlobalsSsmRangeAddress": cie1000IpmcSnoopingConfigMldGlobalsSsmRangeAddress,
       "cie1000IpmcSnoopingConfigMldGlobalsSsmRangeMask": cie1000IpmcSnoopingConfigMldGlobalsSsmRangeMask,
       "cie1000IpmcSnoopingConfigMldGlobalsProxy": cie1000IpmcSnoopingConfigMldGlobalsProxy,
       "cie1000IpmcSnoopingConfigMldGlobalsLeaveProxy": cie1000IpmcSnoopingConfigMldGlobalsLeaveProxy,
       "cie1000IpmcSnoopingConfigMldPortTable": cie1000IpmcSnoopingConfigMldPortTable,
       "cie1000IpmcSnoopingConfigMldPortEntry": cie1000IpmcSnoopingConfigMldPortEntry,
       "cie1000IpmcSnoopingConfigMldPortPortIndex": cie1000IpmcSnoopingConfigMldPortPortIndex,
       "cie1000IpmcSnoopingConfigMldPortAsRouterPort": cie1000IpmcSnoopingConfigMldPortAsRouterPort,
       "cie1000IpmcSnoopingConfigMldPortDoFastLeave": cie1000IpmcSnoopingConfigMldPortDoFastLeave,
       "cie1000IpmcSnoopingConfigMldPortThrottlingNumber": cie1000IpmcSnoopingConfigMldPortThrottlingNumber,
       "cie1000IpmcSnoopingConfigMldPortFilteringProfile": cie1000IpmcSnoopingConfigMldPortFilteringProfile,
       "cie1000IpmcSnoopingConfigMldIfTable": cie1000IpmcSnoopingConfigMldIfTable,
       "cie1000IpmcSnoopingConfigMldIfEntry": cie1000IpmcSnoopingConfigMldIfEntry,
       "cie1000IpmcSnoopingConfigMldIfIfIndex": cie1000IpmcSnoopingConfigMldIfIfIndex,
       "cie1000IpmcSnoopingConfigMldIfAdminState": cie1000IpmcSnoopingConfigMldIfAdminState,
       "cie1000IpmcSnoopingConfigMldIfQuerierElection": cie1000IpmcSnoopingConfigMldIfQuerierElection,
       "cie1000IpmcSnoopingConfigMldIfCompatibility": cie1000IpmcSnoopingConfigMldIfCompatibility,
       "cie1000IpmcSnoopingConfigMldIfPriority": cie1000IpmcSnoopingConfigMldIfPriority,
       "cie1000IpmcSnoopingConfigMldIfRv": cie1000IpmcSnoopingConfigMldIfRv,
       "cie1000IpmcSnoopingConfigMldIfQi": cie1000IpmcSnoopingConfigMldIfQi,
       "cie1000IpmcSnoopingConfigMldIfQri": cie1000IpmcSnoopingConfigMldIfQri,
       "cie1000IpmcSnoopingConfigMldIfLlqi": cie1000IpmcSnoopingConfigMldIfLlqi,
       "cie1000IpmcSnoopingConfigMldIfUri": cie1000IpmcSnoopingConfigMldIfUri,
       "cie1000IpmcSnoopingConfigMldIfAction": cie1000IpmcSnoopingConfigMldIfAction,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditor": cie1000IpmcSnoopingConfigMldIfTableRowEditor,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorIfIndex": cie1000IpmcSnoopingConfigMldIfTableRowEditorIfIndex,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorAdminState": cie1000IpmcSnoopingConfigMldIfTableRowEditorAdminState,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorQuerierElection": cie1000IpmcSnoopingConfigMldIfTableRowEditorQuerierElection,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorCompatibility": cie1000IpmcSnoopingConfigMldIfTableRowEditorCompatibility,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorPriority": cie1000IpmcSnoopingConfigMldIfTableRowEditorPriority,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorRv": cie1000IpmcSnoopingConfigMldIfTableRowEditorRv,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorQi": cie1000IpmcSnoopingConfigMldIfTableRowEditorQi,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorQri": cie1000IpmcSnoopingConfigMldIfTableRowEditorQri,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorLlqi": cie1000IpmcSnoopingConfigMldIfTableRowEditorLlqi,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorUri": cie1000IpmcSnoopingConfigMldIfTableRowEditorUri,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorAction": cie1000IpmcSnoopingConfigMldIfTableRowEditorAction,
       "cie1000IpmcSnoopingStatus": cie1000IpmcSnoopingStatus,
       "cie1000IpmcSnoopingStatusGroupAddressCount": cie1000IpmcSnoopingStatusGroupAddressCount,
       "cie1000IpmcSnoopingStatusGroupAddressCountFromIgmp": cie1000IpmcSnoopingStatusGroupAddressCountFromIgmp,
       "cie1000IpmcSnoopingStatusGroupAddressCountFromMld": cie1000IpmcSnoopingStatusGroupAddressCountFromMld,
       "cie1000IpmcSnoopingStatusIgmpRouterPortTable": cie1000IpmcSnoopingStatusIgmpRouterPortTable,
       "cie1000IpmcSnoopingStatusIgmpRouterPortEntry": cie1000IpmcSnoopingStatusIgmpRouterPortEntry,
       "cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex": cie1000IpmcSnoopingStatusIgmpRouterPortPortIndex,
       "cie1000IpmcSnoopingStatusIgmpRouterPortStatus": cie1000IpmcSnoopingStatusIgmpRouterPortStatus,
       "cie1000IpmcSnoopingStatusIgmpVlanTable": cie1000IpmcSnoopingStatusIgmpVlanTable,
       "cie1000IpmcSnoopingStatusIgmpVlanEntry": cie1000IpmcSnoopingStatusIgmpVlanEntry,
       "cie1000IpmcSnoopingStatusIgmpVlanIfIndex": cie1000IpmcSnoopingStatusIgmpVlanIfIndex,
       "cie1000IpmcSnoopingStatusIgmpVlanQuerierStatus": cie1000IpmcSnoopingStatusIgmpVlanQuerierStatus,
       "cie1000IpmcSnoopingStatusIgmpVlanActiveQuerierAddress": cie1000IpmcSnoopingStatusIgmpVlanActiveQuerierAddress,
       "cie1000IpmcSnoopingStatusIgmpVlanQuerierUptime": cie1000IpmcSnoopingStatusIgmpVlanQuerierUptime,
       "cie1000IpmcSnoopingStatusIgmpVlanQueryInterval": cie1000IpmcSnoopingStatusIgmpVlanQueryInterval,
       "cie1000IpmcSnoopingStatusIgmpVlanStartupQueryCount": cie1000IpmcSnoopingStatusIgmpVlanStartupQueryCount,
       "cie1000IpmcSnoopingStatusIgmpVlanQuerierExpiryTime": cie1000IpmcSnoopingStatusIgmpVlanQuerierExpiryTime,
       "cie1000IpmcSnoopingStatusIgmpVlanQuerierVersion": cie1000IpmcSnoopingStatusIgmpVlanQuerierVersion,
       "cie1000IpmcSnoopingStatusIgmpVlanQuerierPresentTimeout": cie1000IpmcSnoopingStatusIgmpVlanQuerierPresentTimeout,
       "cie1000IpmcSnoopingStatusIgmpVlanHostVersion": cie1000IpmcSnoopingStatusIgmpVlanHostVersion,
       "cie1000IpmcSnoopingStatusIgmpVlanHostPresentTimeout": cie1000IpmcSnoopingStatusIgmpVlanHostPresentTimeout,
       "cie1000IpmcSnoopingStatusIgmpVlanCounterTxQuery": cie1000IpmcSnoopingStatusIgmpVlanCounterTxQuery,
       "cie1000IpmcSnoopingStatusIgmpVlanCounterTxSpecificQuery": cie1000IpmcSnoopingStatusIgmpVlanCounterTxSpecificQuery,
       "cie1000IpmcSnoopingStatusIgmpVlanCounterRxQuery": cie1000IpmcSnoopingStatusIgmpVlanCounterRxQuery,
       "cie1000IpmcSnoopingStatusIgmpVlanCounterRxV1Join": cie1000IpmcSnoopingStatusIgmpVlanCounterRxV1Join,
       "cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Join": cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Join,
       "cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Leave": cie1000IpmcSnoopingStatusIgmpVlanCounterRxV2Leave,
       "cie1000IpmcSnoopingStatusIgmpVlanCounterRxV3Join": cie1000IpmcSnoopingStatusIgmpVlanCounterRxV3Join,
       "cie1000IpmcSnoopingStatusIgmpVlanCounterRxErrors": cie1000IpmcSnoopingStatusIgmpVlanCounterRxErrors,
       "cie1000IpmcSnoopingStatusIgmpGroupAddressTable": cie1000IpmcSnoopingStatusIgmpGroupAddressTable,
       "cie1000IpmcSnoopingStatusIgmpGroupAddressEntry": cie1000IpmcSnoopingStatusIgmpGroupAddressEntry,
       "cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex": cie1000IpmcSnoopingStatusIgmpGroupAddressIfIndex,
       "cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress": cie1000IpmcSnoopingStatusIgmpGroupAddressGroupAddress,
       "cie1000IpmcSnoopingStatusIgmpGroupAddressMemberPorts": cie1000IpmcSnoopingStatusIgmpGroupAddressMemberPorts,
       "cie1000IpmcSnoopingStatusIgmpGroupAddressHardwareSwitch": cie1000IpmcSnoopingStatusIgmpGroupAddressHardwareSwitch,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListTable": cie1000IpmcSnoopingStatusIgmpGroupSrcListTable,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListEntry": cie1000IpmcSnoopingStatusIgmpGroupSrcListEntry,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex": cie1000IpmcSnoopingStatusIgmpGroupSrcListIfIndex,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress": cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupAddress,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex": cie1000IpmcSnoopingStatusIgmpGroupSrcListPortIndex,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress": cie1000IpmcSnoopingStatusIgmpGroupSrcListHostAddress,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupFilterMode": cie1000IpmcSnoopingStatusIgmpGroupSrcListGroupFilterMode,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListFilterTimer": cie1000IpmcSnoopingStatusIgmpGroupSrcListFilterTimer,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceType": cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceType,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceTimer": cie1000IpmcSnoopingStatusIgmpGroupSrcListSourceTimer,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListHardwareFilter": cie1000IpmcSnoopingStatusIgmpGroupSrcListHardwareFilter,
       "cie1000IpmcSnoopingStatusMldRouterPortTable": cie1000IpmcSnoopingStatusMldRouterPortTable,
       "cie1000IpmcSnoopingStatusMldRouterPortEntry": cie1000IpmcSnoopingStatusMldRouterPortEntry,
       "cie1000IpmcSnoopingStatusMldRouterPortPortIndex": cie1000IpmcSnoopingStatusMldRouterPortPortIndex,
       "cie1000IpmcSnoopingStatusMldRouterPortStatus": cie1000IpmcSnoopingStatusMldRouterPortStatus,
       "cie1000IpmcSnoopingStatusMldVlanTable": cie1000IpmcSnoopingStatusMldVlanTable,
       "cie1000IpmcSnoopingStatusMldVlanEntry": cie1000IpmcSnoopingStatusMldVlanEntry,
       "cie1000IpmcSnoopingStatusMldVlanIfIndex": cie1000IpmcSnoopingStatusMldVlanIfIndex,
       "cie1000IpmcSnoopingStatusMldVlanQuerierStatus": cie1000IpmcSnoopingStatusMldVlanQuerierStatus,
       "cie1000IpmcSnoopingStatusMldVlanActiveQuerierAddress": cie1000IpmcSnoopingStatusMldVlanActiveQuerierAddress,
       "cie1000IpmcSnoopingStatusMldVlanQuerierUptime": cie1000IpmcSnoopingStatusMldVlanQuerierUptime,
       "cie1000IpmcSnoopingStatusMldVlanQueryInterval": cie1000IpmcSnoopingStatusMldVlanQueryInterval,
       "cie1000IpmcSnoopingStatusMldVlanStartupQueryCount": cie1000IpmcSnoopingStatusMldVlanStartupQueryCount,
       "cie1000IpmcSnoopingStatusMldVlanQuerierExpiryTime": cie1000IpmcSnoopingStatusMldVlanQuerierExpiryTime,
       "cie1000IpmcSnoopingStatusMldVlanQuerierVersion": cie1000IpmcSnoopingStatusMldVlanQuerierVersion,
       "cie1000IpmcSnoopingStatusMldVlanQuerierPresentTimeout": cie1000IpmcSnoopingStatusMldVlanQuerierPresentTimeout,
       "cie1000IpmcSnoopingStatusMldVlanHostVersion": cie1000IpmcSnoopingStatusMldVlanHostVersion,
       "cie1000IpmcSnoopingStatusMldVlanHostPresentTimeout": cie1000IpmcSnoopingStatusMldVlanHostPresentTimeout,
       "cie1000IpmcSnoopingStatusMldVlanCounterTxQuery": cie1000IpmcSnoopingStatusMldVlanCounterTxQuery,
       "cie1000IpmcSnoopingStatusMldVlanCounterTxSpecificQuery": cie1000IpmcSnoopingStatusMldVlanCounterTxSpecificQuery,
       "cie1000IpmcSnoopingStatusMldVlanCounterRxQuery": cie1000IpmcSnoopingStatusMldVlanCounterRxQuery,
       "cie1000IpmcSnoopingStatusMldVlanCounterRxV1Report": cie1000IpmcSnoopingStatusMldVlanCounterRxV1Report,
       "cie1000IpmcSnoopingStatusMldVlanCounterRxV1Done": cie1000IpmcSnoopingStatusMldVlanCounterRxV1Done,
       "cie1000IpmcSnoopingStatusMldVlanCounterRxV2Report": cie1000IpmcSnoopingStatusMldVlanCounterRxV2Report,
       "cie1000IpmcSnoopingStatusMldVlanCounterRxErrors": cie1000IpmcSnoopingStatusMldVlanCounterRxErrors,
       "cie1000IpmcSnoopingStatusMldGroupAddressTable": cie1000IpmcSnoopingStatusMldGroupAddressTable,
       "cie1000IpmcSnoopingStatusMldGroupAddressEntry": cie1000IpmcSnoopingStatusMldGroupAddressEntry,
       "cie1000IpmcSnoopingStatusMldGroupAddressIfIndex": cie1000IpmcSnoopingStatusMldGroupAddressIfIndex,
       "cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress": cie1000IpmcSnoopingStatusMldGroupAddressGroupAddress,
       "cie1000IpmcSnoopingStatusMldGroupAddressMemberPorts": cie1000IpmcSnoopingStatusMldGroupAddressMemberPorts,
       "cie1000IpmcSnoopingStatusMldGroupAddressHardwareSwitch": cie1000IpmcSnoopingStatusMldGroupAddressHardwareSwitch,
       "cie1000IpmcSnoopingStatusMldGroupSrcListTable": cie1000IpmcSnoopingStatusMldGroupSrcListTable,
       "cie1000IpmcSnoopingStatusMldGroupSrcListEntry": cie1000IpmcSnoopingStatusMldGroupSrcListEntry,
       "cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex": cie1000IpmcSnoopingStatusMldGroupSrcListIfIndex,
       "cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress": cie1000IpmcSnoopingStatusMldGroupSrcListGroupAddress,
       "cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex": cie1000IpmcSnoopingStatusMldGroupSrcListPortIndex,
       "cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress": cie1000IpmcSnoopingStatusMldGroupSrcListHostAddress,
       "cie1000IpmcSnoopingStatusMldGroupSrcListGroupFilterMode": cie1000IpmcSnoopingStatusMldGroupSrcListGroupFilterMode,
       "cie1000IpmcSnoopingStatusMldGroupSrcListFilterTimer": cie1000IpmcSnoopingStatusMldGroupSrcListFilterTimer,
       "cie1000IpmcSnoopingStatusMldGroupSrcListSourceType": cie1000IpmcSnoopingStatusMldGroupSrcListSourceType,
       "cie1000IpmcSnoopingStatusMldGroupSrcListSourceTimer": cie1000IpmcSnoopingStatusMldGroupSrcListSourceTimer,
       "cie1000IpmcSnoopingStatusMldGroupSrcListHardwareFilter": cie1000IpmcSnoopingStatusMldGroupSrcListHardwareFilter,
       "cie1000IpmcSnoopingControl": cie1000IpmcSnoopingControl,
       "cie1000IpmcSnoopingControlStatistics": cie1000IpmcSnoopingControlStatistics,
       "cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndex": cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndex,
       "cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex": cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex,
       "cie1000IpmcSnoopingControlStatisticsMldClearByIfIndex": cie1000IpmcSnoopingControlStatisticsMldClearByIfIndex,
       "cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex": cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex,
       "cie1000IpmcSnoopingMibConformance": cie1000IpmcSnoopingMibConformance,
       "cie1000IpmcSnoopingMibCompliances": cie1000IpmcSnoopingMibCompliances,
       "cie1000IpmcSnoopingMibCompliance": cie1000IpmcSnoopingMibCompliance,
       "cie1000IpmcSnoopingMibGroups": cie1000IpmcSnoopingMibGroups,
       "cie1000IpmcSnoopingConfigIgmpGlobalsInfoGroup": cie1000IpmcSnoopingConfigIgmpGlobalsInfoGroup,
       "cie1000IpmcSnoopingConfigIgmpPortTableInfoGroup": cie1000IpmcSnoopingConfigIgmpPortTableInfoGroup,
       "cie1000IpmcSnoopingConfigIgmpIfTableInfoGroup": cie1000IpmcSnoopingConfigIgmpIfTableInfoGroup,
       "cie1000IpmcSnoopingConfigIgmpIfTableRowEditorInfoGroup": cie1000IpmcSnoopingConfigIgmpIfTableRowEditorInfoGroup,
       "cie1000IpmcSnoopingConfigMldGlobalsInfoGroup": cie1000IpmcSnoopingConfigMldGlobalsInfoGroup,
       "cie1000IpmcSnoopingConfigMldPortTableInfoGroup": cie1000IpmcSnoopingConfigMldPortTableInfoGroup,
       "cie1000IpmcSnoopingConfigMldIfTableInfoGroup": cie1000IpmcSnoopingConfigMldIfTableInfoGroup,
       "cie1000IpmcSnoopingConfigMldIfTableRowEditorInfoGroup": cie1000IpmcSnoopingConfigMldIfTableRowEditorInfoGroup,
       "cie1000IpmcSnoopingStatusGroupAddressCountInfoGroup": cie1000IpmcSnoopingStatusGroupAddressCountInfoGroup,
       "cie1000IpmcSnoopingStatusIgmpRouterPortTableInfoGroup": cie1000IpmcSnoopingStatusIgmpRouterPortTableInfoGroup,
       "cie1000IpmcSnoopingStatusIgmpVlanTableInfoGroup": cie1000IpmcSnoopingStatusIgmpVlanTableInfoGroup,
       "cie1000IpmcSnoopingStatusIgmpGroupAddressTableInfoGroup": cie1000IpmcSnoopingStatusIgmpGroupAddressTableInfoGroup,
       "cie1000IpmcSnoopingStatusIgmpGroupSrcListTableInfoGroup": cie1000IpmcSnoopingStatusIgmpGroupSrcListTableInfoGroup,
       "cie1000IpmcSnoopingStatusMldRouterPortTableInfoGroup": cie1000IpmcSnoopingStatusMldRouterPortTableInfoGroup,
       "cie1000IpmcSnoopingStatusMldVlanTableInfoGroup": cie1000IpmcSnoopingStatusMldVlanTableInfoGroup,
       "cie1000IpmcSnoopingStatusMldGroupAddressTableInfoGroup": cie1000IpmcSnoopingStatusMldGroupAddressTableInfoGroup,
       "cie1000IpmcSnoopingStatusMldGroupSrcListTableInfoGroup": cie1000IpmcSnoopingStatusMldGroupSrcListTableInfoGroup,
       "cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup": cie1000IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup,
       "cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup": cie1000IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup}
)
