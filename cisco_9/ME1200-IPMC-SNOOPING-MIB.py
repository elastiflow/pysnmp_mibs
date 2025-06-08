# SNMP MIB module (ME1200-IPMC-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-IPMC-SNOOPING-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(ME1200DisplayString,
 ME1200InterfaceIndex,
 ME1200PortListStackable,
 ME1200RowEditorState,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex",
    "ME1200PortListStackable",
    "ME1200RowEditorState",
    "ME1200Unsigned8")

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

me1200IpmcSnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMib.setRevisions(
        ("2014-02-11 00:00",
         "2014-02-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200IpmcSnpIgmpInterfaceCompatibility(TextualConvention, Integer32):
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



class ME1200IpmcSnpMldInterfaceCompatibility(TextualConvention, Integer32):
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



class ME1200IpmcSnpIgmpRouterPortStatus(TextualConvention, Integer32):
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



class ME1200IpmcSnpIgmpVlanStatusQuerierStatus(TextualConvention, Integer32):
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



class ME1200IpmcSnpIgmpGroupSrcListGroupFilterMode(TextualConvention, Integer32):
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



class ME1200IpmcSnpIgmpGroupSrcListSourceType(TextualConvention, Integer32):
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



class ME1200IpmcSnpMldRouterPortStatus(TextualConvention, Integer32):
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



class ME1200IpmcSnpMldVlanStatusQuerierStatus(TextualConvention, Integer32):
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



class ME1200IpmcSnpMldGroupSrcListGroupFilterMode(TextualConvention, Integer32):
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



class ME1200IpmcSnpMldGroupSrcListSourceType(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_Me1200IpmcSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingMIBObjects = _Me1200IpmcSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1)
)
_Me1200IpmcSnoopingConfig_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingConfig = _Me1200IpmcSnoopingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2)
)
_Me1200IpmcSnoopingIgmpGlobals_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingIgmpGlobals = _Me1200IpmcSnoopingIgmpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 1)
)
_Me1200IpmcSnoopingIgmpGlobalsAdminState_Type = TruthValue
_Me1200IpmcSnoopingIgmpGlobalsAdminState_Object = MibScalar
me1200IpmcSnoopingIgmpGlobalsAdminState = _Me1200IpmcSnoopingIgmpGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 1, 1),
    _Me1200IpmcSnoopingIgmpGlobalsAdminState_Type()
)
me1200IpmcSnoopingIgmpGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGlobalsAdminState.setStatus("current")
_Me1200IpmcSnoopingIgmpGlobalsUnregisteredFlooding_Type = TruthValue
_Me1200IpmcSnoopingIgmpGlobalsUnregisteredFlooding_Object = MibScalar
me1200IpmcSnoopingIgmpGlobalsUnregisteredFlooding = _Me1200IpmcSnoopingIgmpGlobalsUnregisteredFlooding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 1, 2),
    _Me1200IpmcSnoopingIgmpGlobalsUnregisteredFlooding_Type()
)
me1200IpmcSnoopingIgmpGlobalsUnregisteredFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGlobalsUnregisteredFlooding.setStatus("current")
_Me1200IpmcSnoopingIgmpGlobalsSsmRangeAddress_Type = IpAddress
_Me1200IpmcSnoopingIgmpGlobalsSsmRangeAddress_Object = MibScalar
me1200IpmcSnoopingIgmpGlobalsSsmRangeAddress = _Me1200IpmcSnoopingIgmpGlobalsSsmRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 1, 3),
    _Me1200IpmcSnoopingIgmpGlobalsSsmRangeAddress_Type()
)
me1200IpmcSnoopingIgmpGlobalsSsmRangeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGlobalsSsmRangeAddress.setStatus("current")
_Me1200IpmcSnoopingIgmpGlobalsSsmRangeMask_Type = Unsigned32
_Me1200IpmcSnoopingIgmpGlobalsSsmRangeMask_Object = MibScalar
me1200IpmcSnoopingIgmpGlobalsSsmRangeMask = _Me1200IpmcSnoopingIgmpGlobalsSsmRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 1, 4),
    _Me1200IpmcSnoopingIgmpGlobalsSsmRangeMask_Type()
)
me1200IpmcSnoopingIgmpGlobalsSsmRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGlobalsSsmRangeMask.setStatus("current")
_Me1200IpmcSnoopingIgmpGlobalsProxy_Type = TruthValue
_Me1200IpmcSnoopingIgmpGlobalsProxy_Object = MibScalar
me1200IpmcSnoopingIgmpGlobalsProxy = _Me1200IpmcSnoopingIgmpGlobalsProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 1, 5),
    _Me1200IpmcSnoopingIgmpGlobalsProxy_Type()
)
me1200IpmcSnoopingIgmpGlobalsProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGlobalsProxy.setStatus("current")
_Me1200IpmcSnoopingIgmpGlobalsLeaveProxy_Type = TruthValue
_Me1200IpmcSnoopingIgmpGlobalsLeaveProxy_Object = MibScalar
me1200IpmcSnoopingIgmpGlobalsLeaveProxy = _Me1200IpmcSnoopingIgmpGlobalsLeaveProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 1, 6),
    _Me1200IpmcSnoopingIgmpGlobalsLeaveProxy_Type()
)
me1200IpmcSnoopingIgmpGlobalsLeaveProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGlobalsLeaveProxy.setStatus("current")
_Me1200IpmcSnoopingIgmpPortTable_Object = MibTable
me1200IpmcSnoopingIgmpPortTable = _Me1200IpmcSnoopingIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpPortTable.setStatus("current")
_Me1200IpmcSnoopingIgmpPortEntry_Object = MibTableRow
me1200IpmcSnoopingIgmpPortEntry = _Me1200IpmcSnoopingIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 2, 1)
)
me1200IpmcSnoopingIgmpPortEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpPortPortIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpPortEntry.setStatus("current")
_Me1200IpmcSnoopingIgmpPortPortIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingIgmpPortPortIndex_Object = MibTableColumn
me1200IpmcSnoopingIgmpPortPortIndex = _Me1200IpmcSnoopingIgmpPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 2, 1, 1),
    _Me1200IpmcSnoopingIgmpPortPortIndex_Type()
)
me1200IpmcSnoopingIgmpPortPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpPortPortIndex.setStatus("current")
_Me1200IpmcSnoopingIgmpPortAsRouterPort_Type = TruthValue
_Me1200IpmcSnoopingIgmpPortAsRouterPort_Object = MibTableColumn
me1200IpmcSnoopingIgmpPortAsRouterPort = _Me1200IpmcSnoopingIgmpPortAsRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 2, 1, 2),
    _Me1200IpmcSnoopingIgmpPortAsRouterPort_Type()
)
me1200IpmcSnoopingIgmpPortAsRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpPortAsRouterPort.setStatus("current")
_Me1200IpmcSnoopingIgmpPortDoFastLeave_Type = TruthValue
_Me1200IpmcSnoopingIgmpPortDoFastLeave_Object = MibTableColumn
me1200IpmcSnoopingIgmpPortDoFastLeave = _Me1200IpmcSnoopingIgmpPortDoFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 2, 1, 3),
    _Me1200IpmcSnoopingIgmpPortDoFastLeave_Type()
)
me1200IpmcSnoopingIgmpPortDoFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpPortDoFastLeave.setStatus("current")
_Me1200IpmcSnoopingIgmpPortThrottlingNumber_Type = Integer32
_Me1200IpmcSnoopingIgmpPortThrottlingNumber_Object = MibTableColumn
me1200IpmcSnoopingIgmpPortThrottlingNumber = _Me1200IpmcSnoopingIgmpPortThrottlingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 2, 1, 4),
    _Me1200IpmcSnoopingIgmpPortThrottlingNumber_Type()
)
me1200IpmcSnoopingIgmpPortThrottlingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpPortThrottlingNumber.setStatus("current")


class _Me1200IpmcSnoopingIgmpPortFilteringProfile_Type(ME1200DisplayString):
    """Custom type me1200IpmcSnoopingIgmpPortFilteringProfile based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcSnoopingIgmpPortFilteringProfile_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcSnoopingIgmpPortFilteringProfile_Object = MibTableColumn
me1200IpmcSnoopingIgmpPortFilteringProfile = _Me1200IpmcSnoopingIgmpPortFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 2, 1, 5),
    _Me1200IpmcSnoopingIgmpPortFilteringProfile_Type()
)
me1200IpmcSnoopingIgmpPortFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpPortFilteringProfile.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTable_Object = MibTable
me1200IpmcSnoopingIgmpInterfaceTable = _Me1200IpmcSnoopingIgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTable.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceEntry_Object = MibTableRow
me1200IpmcSnoopingIgmpInterfaceEntry = _Me1200IpmcSnoopingIgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1)
)
me1200IpmcSnoopingIgmpInterfaceEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceEntry.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingIgmpInterfaceIfIndex_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceIfIndex = _Me1200IpmcSnoopingIgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 1),
    _Me1200IpmcSnoopingIgmpInterfaceIfIndex_Type()
)
me1200IpmcSnoopingIgmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceIfIndex.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceAdminState_Type = TruthValue
_Me1200IpmcSnoopingIgmpInterfaceAdminState_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceAdminState = _Me1200IpmcSnoopingIgmpInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 2),
    _Me1200IpmcSnoopingIgmpInterfaceAdminState_Type()
)
me1200IpmcSnoopingIgmpInterfaceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceAdminState.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceQuerierElection_Type = TruthValue
_Me1200IpmcSnoopingIgmpInterfaceQuerierElection_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceQuerierElection = _Me1200IpmcSnoopingIgmpInterfaceQuerierElection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 3),
    _Me1200IpmcSnoopingIgmpInterfaceQuerierElection_Type()
)
me1200IpmcSnoopingIgmpInterfaceQuerierElection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceQuerierElection.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceQuerierAddress_Type = IpAddress
_Me1200IpmcSnoopingIgmpInterfaceQuerierAddress_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceQuerierAddress = _Me1200IpmcSnoopingIgmpInterfaceQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 4),
    _Me1200IpmcSnoopingIgmpInterfaceQuerierAddress_Type()
)
me1200IpmcSnoopingIgmpInterfaceQuerierAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceQuerierAddress.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceCompatibility_Type = ME1200IpmcSnpIgmpInterfaceCompatibility
_Me1200IpmcSnoopingIgmpInterfaceCompatibility_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceCompatibility = _Me1200IpmcSnoopingIgmpInterfaceCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 5),
    _Me1200IpmcSnoopingIgmpInterfaceCompatibility_Type()
)
me1200IpmcSnoopingIgmpInterfaceCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceCompatibility.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfacePriority_Type = ME1200Unsigned8
_Me1200IpmcSnoopingIgmpInterfacePriority_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfacePriority = _Me1200IpmcSnoopingIgmpInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 6),
    _Me1200IpmcSnoopingIgmpInterfacePriority_Type()
)
me1200IpmcSnoopingIgmpInterfacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfacePriority.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceRv_Type = Unsigned32
_Me1200IpmcSnoopingIgmpInterfaceRv_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceRv = _Me1200IpmcSnoopingIgmpInterfaceRv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 7),
    _Me1200IpmcSnoopingIgmpInterfaceRv_Type()
)
me1200IpmcSnoopingIgmpInterfaceRv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceRv.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceQi_Type = Unsigned32
_Me1200IpmcSnoopingIgmpInterfaceQi_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceQi = _Me1200IpmcSnoopingIgmpInterfaceQi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 8),
    _Me1200IpmcSnoopingIgmpInterfaceQi_Type()
)
me1200IpmcSnoopingIgmpInterfaceQi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceQi.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceQri_Type = Unsigned32
_Me1200IpmcSnoopingIgmpInterfaceQri_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceQri = _Me1200IpmcSnoopingIgmpInterfaceQri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 9),
    _Me1200IpmcSnoopingIgmpInterfaceQri_Type()
)
me1200IpmcSnoopingIgmpInterfaceQri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceQri.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceLmqi_Type = Unsigned32
_Me1200IpmcSnoopingIgmpInterfaceLmqi_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceLmqi = _Me1200IpmcSnoopingIgmpInterfaceLmqi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 10),
    _Me1200IpmcSnoopingIgmpInterfaceLmqi_Type()
)
me1200IpmcSnoopingIgmpInterfaceLmqi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceLmqi.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceUri_Type = Unsigned32
_Me1200IpmcSnoopingIgmpInterfaceUri_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceUri = _Me1200IpmcSnoopingIgmpInterfaceUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 11),
    _Me1200IpmcSnoopingIgmpInterfaceUri_Type()
)
me1200IpmcSnoopingIgmpInterfaceUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceUri.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceAction_Type = ME1200RowEditorState
_Me1200IpmcSnoopingIgmpInterfaceAction_Object = MibTableColumn
me1200IpmcSnoopingIgmpInterfaceAction = _Me1200IpmcSnoopingIgmpInterfaceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 3, 1, 100),
    _Me1200IpmcSnoopingIgmpInterfaceAction_Type()
)
me1200IpmcSnoopingIgmpInterfaceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceAction.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditor_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingIgmpInterfaceTableRowEditor = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4)
)
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorIfIndex_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorIfIndex = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 1),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorIfIndex_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorIfIndex.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorAdminState_Type = TruthValue
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorAdminState_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorAdminState = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 2),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorAdminState_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorAdminState.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierElection_Type = TruthValue
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierElection_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierElection = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierElection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 3),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierElection_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierElection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierElection.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierAddress_Type = IpAddress
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierAddress_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierAddress = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 4),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierAddress_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierAddress.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorCompatibility_Type = ME1200IpmcSnpIgmpInterfaceCompatibility
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorCompatibility_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorCompatibility = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 5),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorCompatibility_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorCompatibility.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorPriority_Type = ME1200Unsigned8
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorPriority_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorPriority = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 6),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorPriority_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorPriority.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorRv_Type = Unsigned32
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorRv_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorRv = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorRv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 7),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorRv_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorRv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorRv.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQi_Type = Unsigned32
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQi_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorQi = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 8),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQi_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorQi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorQi.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQri_Type = Unsigned32
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQri_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorQri = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 9),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorQri_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorQri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorQri.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorLmqi_Type = Unsigned32
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorLmqi_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorLmqi = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorLmqi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 10),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorLmqi_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorLmqi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorLmqi.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorUri_Type = Unsigned32
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorUri_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorUri = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 11),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorUri_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorUri.setStatus("current")
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorAction_Type = ME1200RowEditorState
_Me1200IpmcSnoopingIgmpInterfaceTableRowEditorAction_Object = MibScalar
me1200IpmcSnoopingIgmpInterfaceTableRowEditorAction = _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 4, 100),
    _Me1200IpmcSnoopingIgmpInterfaceTableRowEditorAction_Type()
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorAction.setStatus("current")
_Me1200IpmcSnoopingMldGlobals_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingMldGlobals = _Me1200IpmcSnoopingMldGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 5)
)
_Me1200IpmcSnoopingMldGlobalsAdminState_Type = TruthValue
_Me1200IpmcSnoopingMldGlobalsAdminState_Object = MibScalar
me1200IpmcSnoopingMldGlobalsAdminState = _Me1200IpmcSnoopingMldGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 5, 1),
    _Me1200IpmcSnoopingMldGlobalsAdminState_Type()
)
me1200IpmcSnoopingMldGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGlobalsAdminState.setStatus("current")
_Me1200IpmcSnoopingMldGlobalsUnregisteredFlooding_Type = TruthValue
_Me1200IpmcSnoopingMldGlobalsUnregisteredFlooding_Object = MibScalar
me1200IpmcSnoopingMldGlobalsUnregisteredFlooding = _Me1200IpmcSnoopingMldGlobalsUnregisteredFlooding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 5, 2),
    _Me1200IpmcSnoopingMldGlobalsUnregisteredFlooding_Type()
)
me1200IpmcSnoopingMldGlobalsUnregisteredFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGlobalsUnregisteredFlooding.setStatus("current")
_Me1200IpmcSnoopingMldGlobalsSsmRangeAddress_Type = InetAddressIPv6
_Me1200IpmcSnoopingMldGlobalsSsmRangeAddress_Object = MibScalar
me1200IpmcSnoopingMldGlobalsSsmRangeAddress = _Me1200IpmcSnoopingMldGlobalsSsmRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 5, 3),
    _Me1200IpmcSnoopingMldGlobalsSsmRangeAddress_Type()
)
me1200IpmcSnoopingMldGlobalsSsmRangeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGlobalsSsmRangeAddress.setStatus("current")
_Me1200IpmcSnoopingMldGlobalsSsmRangeMask_Type = Unsigned32
_Me1200IpmcSnoopingMldGlobalsSsmRangeMask_Object = MibScalar
me1200IpmcSnoopingMldGlobalsSsmRangeMask = _Me1200IpmcSnoopingMldGlobalsSsmRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 5, 4),
    _Me1200IpmcSnoopingMldGlobalsSsmRangeMask_Type()
)
me1200IpmcSnoopingMldGlobalsSsmRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGlobalsSsmRangeMask.setStatus("current")
_Me1200IpmcSnoopingMldGlobalsProxy_Type = TruthValue
_Me1200IpmcSnoopingMldGlobalsProxy_Object = MibScalar
me1200IpmcSnoopingMldGlobalsProxy = _Me1200IpmcSnoopingMldGlobalsProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 5, 5),
    _Me1200IpmcSnoopingMldGlobalsProxy_Type()
)
me1200IpmcSnoopingMldGlobalsProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGlobalsProxy.setStatus("current")
_Me1200IpmcSnoopingMldGlobalsLeaveProxy_Type = TruthValue
_Me1200IpmcSnoopingMldGlobalsLeaveProxy_Object = MibScalar
me1200IpmcSnoopingMldGlobalsLeaveProxy = _Me1200IpmcSnoopingMldGlobalsLeaveProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 5, 6),
    _Me1200IpmcSnoopingMldGlobalsLeaveProxy_Type()
)
me1200IpmcSnoopingMldGlobalsLeaveProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGlobalsLeaveProxy.setStatus("current")
_Me1200IpmcSnoopingMldPortTable_Object = MibTable
me1200IpmcSnoopingMldPortTable = _Me1200IpmcSnoopingMldPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 6)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldPortTable.setStatus("current")
_Me1200IpmcSnoopingMldPortEntry_Object = MibTableRow
me1200IpmcSnoopingMldPortEntry = _Me1200IpmcSnoopingMldPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 6, 1)
)
me1200IpmcSnoopingMldPortEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldPortPortIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldPortEntry.setStatus("current")
_Me1200IpmcSnoopingMldPortPortIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingMldPortPortIndex_Object = MibTableColumn
me1200IpmcSnoopingMldPortPortIndex = _Me1200IpmcSnoopingMldPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 6, 1, 1),
    _Me1200IpmcSnoopingMldPortPortIndex_Type()
)
me1200IpmcSnoopingMldPortPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldPortPortIndex.setStatus("current")
_Me1200IpmcSnoopingMldPortAsRouterPort_Type = TruthValue
_Me1200IpmcSnoopingMldPortAsRouterPort_Object = MibTableColumn
me1200IpmcSnoopingMldPortAsRouterPort = _Me1200IpmcSnoopingMldPortAsRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 6, 1, 2),
    _Me1200IpmcSnoopingMldPortAsRouterPort_Type()
)
me1200IpmcSnoopingMldPortAsRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldPortAsRouterPort.setStatus("current")
_Me1200IpmcSnoopingMldPortDoFastLeave_Type = TruthValue
_Me1200IpmcSnoopingMldPortDoFastLeave_Object = MibTableColumn
me1200IpmcSnoopingMldPortDoFastLeave = _Me1200IpmcSnoopingMldPortDoFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 6, 1, 3),
    _Me1200IpmcSnoopingMldPortDoFastLeave_Type()
)
me1200IpmcSnoopingMldPortDoFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldPortDoFastLeave.setStatus("current")
_Me1200IpmcSnoopingMldPortThrottlingNumber_Type = Integer32
_Me1200IpmcSnoopingMldPortThrottlingNumber_Object = MibTableColumn
me1200IpmcSnoopingMldPortThrottlingNumber = _Me1200IpmcSnoopingMldPortThrottlingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 6, 1, 4),
    _Me1200IpmcSnoopingMldPortThrottlingNumber_Type()
)
me1200IpmcSnoopingMldPortThrottlingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldPortThrottlingNumber.setStatus("current")


class _Me1200IpmcSnoopingMldPortFilteringProfile_Type(ME1200DisplayString):
    """Custom type me1200IpmcSnoopingMldPortFilteringProfile based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcSnoopingMldPortFilteringProfile_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcSnoopingMldPortFilteringProfile_Object = MibTableColumn
me1200IpmcSnoopingMldPortFilteringProfile = _Me1200IpmcSnoopingMldPortFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 6, 1, 5),
    _Me1200IpmcSnoopingMldPortFilteringProfile_Type()
)
me1200IpmcSnoopingMldPortFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldPortFilteringProfile.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTable_Object = MibTable
me1200IpmcSnoopingMldInterfaceTable = _Me1200IpmcSnoopingMldInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTable.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceEntry_Object = MibTableRow
me1200IpmcSnoopingMldInterfaceEntry = _Me1200IpmcSnoopingMldInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1)
)
me1200IpmcSnoopingMldInterfaceEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceEntry.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingMldInterfaceIfIndex_Object = MibTableColumn
me1200IpmcSnoopingMldInterfaceIfIndex = _Me1200IpmcSnoopingMldInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 1),
    _Me1200IpmcSnoopingMldInterfaceIfIndex_Type()
)
me1200IpmcSnoopingMldInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceIfIndex.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceAdminState_Type = TruthValue
_Me1200IpmcSnoopingMldInterfaceAdminState_Object = MibTableColumn
me1200IpmcSnoopingMldInterfaceAdminState = _Me1200IpmcSnoopingMldInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 2),
    _Me1200IpmcSnoopingMldInterfaceAdminState_Type()
)
me1200IpmcSnoopingMldInterfaceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceAdminState.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceQuerierElection_Type = TruthValue
_Me1200IpmcSnoopingMldInterfaceQuerierElection_Object = MibTableColumn
me1200IpmcSnoopingMldInterfaceQuerierElection = _Me1200IpmcSnoopingMldInterfaceQuerierElection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 3),
    _Me1200IpmcSnoopingMldInterfaceQuerierElection_Type()
)
me1200IpmcSnoopingMldInterfaceQuerierElection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceQuerierElection.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceCompatibility_Type = ME1200IpmcSnpMldInterfaceCompatibility
_Me1200IpmcSnoopingMldInterfaceCompatibility_Object = MibTableColumn
me1200IpmcSnoopingMldInterfaceCompatibility = _Me1200IpmcSnoopingMldInterfaceCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 4),
    _Me1200IpmcSnoopingMldInterfaceCompatibility_Type()
)
me1200IpmcSnoopingMldInterfaceCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceCompatibility.setStatus("current")
_Me1200IpmcSnoopingMldInterfacePriority_Type = ME1200Unsigned8
_Me1200IpmcSnoopingMldInterfacePriority_Object = MibTableColumn
me1200IpmcSnoopingMldInterfacePriority = _Me1200IpmcSnoopingMldInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 5),
    _Me1200IpmcSnoopingMldInterfacePriority_Type()
)
me1200IpmcSnoopingMldInterfacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfacePriority.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceRv_Type = Unsigned32
_Me1200IpmcSnoopingMldInterfaceRv_Object = MibTableColumn
me1200IpmcSnoopingMldInterfaceRv = _Me1200IpmcSnoopingMldInterfaceRv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 6),
    _Me1200IpmcSnoopingMldInterfaceRv_Type()
)
me1200IpmcSnoopingMldInterfaceRv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceRv.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceQi_Type = Unsigned32
_Me1200IpmcSnoopingMldInterfaceQi_Object = MibTableColumn
me1200IpmcSnoopingMldInterfaceQi = _Me1200IpmcSnoopingMldInterfaceQi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 7),
    _Me1200IpmcSnoopingMldInterfaceQi_Type()
)
me1200IpmcSnoopingMldInterfaceQi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceQi.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceQri_Type = Unsigned32
_Me1200IpmcSnoopingMldInterfaceQri_Object = MibTableColumn
me1200IpmcSnoopingMldInterfaceQri = _Me1200IpmcSnoopingMldInterfaceQri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 8),
    _Me1200IpmcSnoopingMldInterfaceQri_Type()
)
me1200IpmcSnoopingMldInterfaceQri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceQri.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceLlqi_Type = Unsigned32
_Me1200IpmcSnoopingMldInterfaceLlqi_Object = MibTableColumn
me1200IpmcSnoopingMldInterfaceLlqi = _Me1200IpmcSnoopingMldInterfaceLlqi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 9),
    _Me1200IpmcSnoopingMldInterfaceLlqi_Type()
)
me1200IpmcSnoopingMldInterfaceLlqi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceLlqi.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceUri_Type = Unsigned32
_Me1200IpmcSnoopingMldInterfaceUri_Object = MibTableColumn
me1200IpmcSnoopingMldInterfaceUri = _Me1200IpmcSnoopingMldInterfaceUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 10),
    _Me1200IpmcSnoopingMldInterfaceUri_Type()
)
me1200IpmcSnoopingMldInterfaceUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceUri.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceAction_Type = ME1200RowEditorState
_Me1200IpmcSnoopingMldInterfaceAction_Object = MibTableColumn
me1200IpmcSnoopingMldInterfaceAction = _Me1200IpmcSnoopingMldInterfaceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 7, 1, 100),
    _Me1200IpmcSnoopingMldInterfaceAction_Type()
)
me1200IpmcSnoopingMldInterfaceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceAction.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditor_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingMldInterfaceTableRowEditor = _Me1200IpmcSnoopingMldInterfaceTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8)
)
_Me1200IpmcSnoopingMldInterfaceTableRowEditorIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingMldInterfaceTableRowEditorIfIndex_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorIfIndex = _Me1200IpmcSnoopingMldInterfaceTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 1),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorIfIndex_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorIfIndex.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditorAdminState_Type = TruthValue
_Me1200IpmcSnoopingMldInterfaceTableRowEditorAdminState_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorAdminState = _Me1200IpmcSnoopingMldInterfaceTableRowEditorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 2),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorAdminState_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorAdminState.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditorQuerierElection_Type = TruthValue
_Me1200IpmcSnoopingMldInterfaceTableRowEditorQuerierElection_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorQuerierElection = _Me1200IpmcSnoopingMldInterfaceTableRowEditorQuerierElection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 3),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorQuerierElection_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorQuerierElection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorQuerierElection.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditorCompatibility_Type = ME1200IpmcSnpMldInterfaceCompatibility
_Me1200IpmcSnoopingMldInterfaceTableRowEditorCompatibility_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorCompatibility = _Me1200IpmcSnoopingMldInterfaceTableRowEditorCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 4),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorCompatibility_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorCompatibility.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditorPriority_Type = ME1200Unsigned8
_Me1200IpmcSnoopingMldInterfaceTableRowEditorPriority_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorPriority = _Me1200IpmcSnoopingMldInterfaceTableRowEditorPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 5),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorPriority_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorPriority.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditorRv_Type = Unsigned32
_Me1200IpmcSnoopingMldInterfaceTableRowEditorRv_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorRv = _Me1200IpmcSnoopingMldInterfaceTableRowEditorRv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 6),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorRv_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorRv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorRv.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditorQi_Type = Unsigned32
_Me1200IpmcSnoopingMldInterfaceTableRowEditorQi_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorQi = _Me1200IpmcSnoopingMldInterfaceTableRowEditorQi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 7),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorQi_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorQi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorQi.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditorQri_Type = Unsigned32
_Me1200IpmcSnoopingMldInterfaceTableRowEditorQri_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorQri = _Me1200IpmcSnoopingMldInterfaceTableRowEditorQri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 8),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorQri_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorQri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorQri.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditorLlqi_Type = Unsigned32
_Me1200IpmcSnoopingMldInterfaceTableRowEditorLlqi_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorLlqi = _Me1200IpmcSnoopingMldInterfaceTableRowEditorLlqi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 9),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorLlqi_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorLlqi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorLlqi.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditorUri_Type = Unsigned32
_Me1200IpmcSnoopingMldInterfaceTableRowEditorUri_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorUri = _Me1200IpmcSnoopingMldInterfaceTableRowEditorUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 10),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorUri_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorUri.setStatus("current")
_Me1200IpmcSnoopingMldInterfaceTableRowEditorAction_Type = ME1200RowEditorState
_Me1200IpmcSnoopingMldInterfaceTableRowEditorAction_Object = MibScalar
me1200IpmcSnoopingMldInterfaceTableRowEditorAction = _Me1200IpmcSnoopingMldInterfaceTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 2, 8, 100),
    _Me1200IpmcSnoopingMldInterfaceTableRowEditorAction_Type()
)
me1200IpmcSnoopingMldInterfaceTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorAction.setStatus("current")
_Me1200IpmcSnoopingStatus_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingStatus = _Me1200IpmcSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3)
)
_Me1200IpmcSnoopingGroupAddressCount_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingGroupAddressCount = _Me1200IpmcSnoopingGroupAddressCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 1)
)
_Me1200IpmcSnoopingGroupAddressCountFromIgmp_Type = Unsigned32
_Me1200IpmcSnoopingGroupAddressCountFromIgmp_Object = MibScalar
me1200IpmcSnoopingGroupAddressCountFromIgmp = _Me1200IpmcSnoopingGroupAddressCountFromIgmp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 1, 1),
    _Me1200IpmcSnoopingGroupAddressCountFromIgmp_Type()
)
me1200IpmcSnoopingGroupAddressCountFromIgmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingGroupAddressCountFromIgmp.setStatus("current")
_Me1200IpmcSnoopingGroupAddressCountFromMld_Type = Unsigned32
_Me1200IpmcSnoopingGroupAddressCountFromMld_Object = MibScalar
me1200IpmcSnoopingGroupAddressCountFromMld = _Me1200IpmcSnoopingGroupAddressCountFromMld_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 1, 2),
    _Me1200IpmcSnoopingGroupAddressCountFromMld_Type()
)
me1200IpmcSnoopingGroupAddressCountFromMld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingGroupAddressCountFromMld.setStatus("current")
_Me1200IpmcSnoopingIgmpRouterPortTable_Object = MibTable
me1200IpmcSnoopingIgmpRouterPortTable = _Me1200IpmcSnoopingIgmpRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpRouterPortTable.setStatus("current")
_Me1200IpmcSnoopingIgmpRouterPortEntry_Object = MibTableRow
me1200IpmcSnoopingIgmpRouterPortEntry = _Me1200IpmcSnoopingIgmpRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 2, 1)
)
me1200IpmcSnoopingIgmpRouterPortEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpRouterPortPortIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpRouterPortEntry.setStatus("current")
_Me1200IpmcSnoopingIgmpRouterPortPortIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingIgmpRouterPortPortIndex_Object = MibTableColumn
me1200IpmcSnoopingIgmpRouterPortPortIndex = _Me1200IpmcSnoopingIgmpRouterPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 2, 1, 1),
    _Me1200IpmcSnoopingIgmpRouterPortPortIndex_Type()
)
me1200IpmcSnoopingIgmpRouterPortPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpRouterPortPortIndex.setStatus("current")
_Me1200IpmcSnoopingIgmpRouterPortStatus_Type = ME1200IpmcSnpIgmpRouterPortStatus
_Me1200IpmcSnoopingIgmpRouterPortStatus_Object = MibTableColumn
me1200IpmcSnoopingIgmpRouterPortStatus = _Me1200IpmcSnoopingIgmpRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 2, 1, 2),
    _Me1200IpmcSnoopingIgmpRouterPortStatus_Type()
)
me1200IpmcSnoopingIgmpRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpRouterPortStatus.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusTable_Object = MibTable
me1200IpmcSnoopingIgmpVlanStatusTable = _Me1200IpmcSnoopingIgmpVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusTable.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusEntry_Object = MibTableRow
me1200IpmcSnoopingIgmpVlanStatusEntry = _Me1200IpmcSnoopingIgmpVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1)
)
me1200IpmcSnoopingIgmpVlanStatusEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusEntry.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingIgmpVlanStatusIfIndex_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusIfIndex = _Me1200IpmcSnoopingIgmpVlanStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 1),
    _Me1200IpmcSnoopingIgmpVlanStatusIfIndex_Type()
)
me1200IpmcSnoopingIgmpVlanStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusIfIndex.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusQuerierStatus_Type = ME1200IpmcSnpIgmpVlanStatusQuerierStatus
_Me1200IpmcSnoopingIgmpVlanStatusQuerierStatus_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusQuerierStatus = _Me1200IpmcSnoopingIgmpVlanStatusQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 2),
    _Me1200IpmcSnoopingIgmpVlanStatusQuerierStatus_Type()
)
me1200IpmcSnoopingIgmpVlanStatusQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusQuerierStatus.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusActiveQuerierAddress_Type = IpAddress
_Me1200IpmcSnoopingIgmpVlanStatusActiveQuerierAddress_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusActiveQuerierAddress = _Me1200IpmcSnoopingIgmpVlanStatusActiveQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 3),
    _Me1200IpmcSnoopingIgmpVlanStatusActiveQuerierAddress_Type()
)
me1200IpmcSnoopingIgmpVlanStatusActiveQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusActiveQuerierAddress.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusQuerierUptime_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusQuerierUptime_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusQuerierUptime = _Me1200IpmcSnoopingIgmpVlanStatusQuerierUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 4),
    _Me1200IpmcSnoopingIgmpVlanStatusQuerierUptime_Type()
)
me1200IpmcSnoopingIgmpVlanStatusQuerierUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusQuerierUptime.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusQueryInterval_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusQueryInterval_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusQueryInterval = _Me1200IpmcSnoopingIgmpVlanStatusQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 5),
    _Me1200IpmcSnoopingIgmpVlanStatusQueryInterval_Type()
)
me1200IpmcSnoopingIgmpVlanStatusQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusQueryInterval.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusStartupQueryCount_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusStartupQueryCount_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusStartupQueryCount = _Me1200IpmcSnoopingIgmpVlanStatusStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 6),
    _Me1200IpmcSnoopingIgmpVlanStatusStartupQueryCount_Type()
)
me1200IpmcSnoopingIgmpVlanStatusStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusStartupQueryCount.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusQuerierExpiryTime_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusQuerierExpiryTime_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusQuerierExpiryTime = _Me1200IpmcSnoopingIgmpVlanStatusQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 7),
    _Me1200IpmcSnoopingIgmpVlanStatusQuerierExpiryTime_Type()
)
me1200IpmcSnoopingIgmpVlanStatusQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusQuerierExpiryTime.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusQuerierVersion_Type = ME1200Unsigned8
_Me1200IpmcSnoopingIgmpVlanStatusQuerierVersion_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusQuerierVersion = _Me1200IpmcSnoopingIgmpVlanStatusQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 8),
    _Me1200IpmcSnoopingIgmpVlanStatusQuerierVersion_Type()
)
me1200IpmcSnoopingIgmpVlanStatusQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusQuerierVersion.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusQuerierPresentTimeout_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusQuerierPresentTimeout_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusQuerierPresentTimeout = _Me1200IpmcSnoopingIgmpVlanStatusQuerierPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 9),
    _Me1200IpmcSnoopingIgmpVlanStatusQuerierPresentTimeout_Type()
)
me1200IpmcSnoopingIgmpVlanStatusQuerierPresentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusQuerierPresentTimeout.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusHostVersion_Type = ME1200Unsigned8
_Me1200IpmcSnoopingIgmpVlanStatusHostVersion_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusHostVersion = _Me1200IpmcSnoopingIgmpVlanStatusHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 10),
    _Me1200IpmcSnoopingIgmpVlanStatusHostVersion_Type()
)
me1200IpmcSnoopingIgmpVlanStatusHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusHostVersion.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusHostPresentTimeout_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusHostPresentTimeout_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusHostPresentTimeout = _Me1200IpmcSnoopingIgmpVlanStatusHostPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 11),
    _Me1200IpmcSnoopingIgmpVlanStatusHostPresentTimeout_Type()
)
me1200IpmcSnoopingIgmpVlanStatusHostPresentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusHostPresentTimeout.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusCounterTxQuery_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusCounterTxQuery_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusCounterTxQuery = _Me1200IpmcSnoopingIgmpVlanStatusCounterTxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 12),
    _Me1200IpmcSnoopingIgmpVlanStatusCounterTxQuery_Type()
)
me1200IpmcSnoopingIgmpVlanStatusCounterTxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusCounterTxQuery.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusCounterTxSpecificQuery_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusCounterTxSpecificQuery_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusCounterTxSpecificQuery = _Me1200IpmcSnoopingIgmpVlanStatusCounterTxSpecificQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 13),
    _Me1200IpmcSnoopingIgmpVlanStatusCounterTxSpecificQuery_Type()
)
me1200IpmcSnoopingIgmpVlanStatusCounterTxSpecificQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusCounterTxSpecificQuery.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxQuery_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxQuery_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusCounterRxQuery = _Me1200IpmcSnoopingIgmpVlanStatusCounterRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 14),
    _Me1200IpmcSnoopingIgmpVlanStatusCounterRxQuery_Type()
)
me1200IpmcSnoopingIgmpVlanStatusCounterRxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusCounterRxQuery.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxV1Join_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxV1Join_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusCounterRxV1Join = _Me1200IpmcSnoopingIgmpVlanStatusCounterRxV1Join_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 15),
    _Me1200IpmcSnoopingIgmpVlanStatusCounterRxV1Join_Type()
)
me1200IpmcSnoopingIgmpVlanStatusCounterRxV1Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusCounterRxV1Join.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Join_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Join_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Join = _Me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Join_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 16),
    _Me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Join_Type()
)
me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Join.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Leave_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Leave_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Leave = _Me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Leave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 17),
    _Me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Leave_Type()
)
me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Leave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Leave.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxV3Join_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxV3Join_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusCounterRxV3Join = _Me1200IpmcSnoopingIgmpVlanStatusCounterRxV3Join_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 18),
    _Me1200IpmcSnoopingIgmpVlanStatusCounterRxV3Join_Type()
)
me1200IpmcSnoopingIgmpVlanStatusCounterRxV3Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusCounterRxV3Join.setStatus("current")
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxErrors_Type = Unsigned32
_Me1200IpmcSnoopingIgmpVlanStatusCounterRxErrors_Object = MibTableColumn
me1200IpmcSnoopingIgmpVlanStatusCounterRxErrors = _Me1200IpmcSnoopingIgmpVlanStatusCounterRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 3, 1, 19),
    _Me1200IpmcSnoopingIgmpVlanStatusCounterRxErrors_Type()
)
me1200IpmcSnoopingIgmpVlanStatusCounterRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusCounterRxErrors.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupAddressTable_Object = MibTable
me1200IpmcSnoopingIgmpGroupAddressTable = _Me1200IpmcSnoopingIgmpGroupAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 4)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupAddressTable.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupAddressEntry_Object = MibTableRow
me1200IpmcSnoopingIgmpGroupAddressEntry = _Me1200IpmcSnoopingIgmpGroupAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 4, 1)
)
me1200IpmcSnoopingIgmpGroupAddressEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupAddressIfIndex"),
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupAddressGroupAddress"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupAddressEntry.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupAddressIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingIgmpGroupAddressIfIndex_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupAddressIfIndex = _Me1200IpmcSnoopingIgmpGroupAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 4, 1, 1),
    _Me1200IpmcSnoopingIgmpGroupAddressIfIndex_Type()
)
me1200IpmcSnoopingIgmpGroupAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupAddressIfIndex.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupAddressGroupAddress_Type = IpAddress
_Me1200IpmcSnoopingIgmpGroupAddressGroupAddress_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupAddressGroupAddress = _Me1200IpmcSnoopingIgmpGroupAddressGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 4, 1, 2),
    _Me1200IpmcSnoopingIgmpGroupAddressGroupAddress_Type()
)
me1200IpmcSnoopingIgmpGroupAddressGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupAddressGroupAddress.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupAddressMemberPorts_Type = ME1200PortListStackable
_Me1200IpmcSnoopingIgmpGroupAddressMemberPorts_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupAddressMemberPorts = _Me1200IpmcSnoopingIgmpGroupAddressMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 4, 1, 3),
    _Me1200IpmcSnoopingIgmpGroupAddressMemberPorts_Type()
)
me1200IpmcSnoopingIgmpGroupAddressMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupAddressMemberPorts.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupAddressHardwareSwitch_Type = TruthValue
_Me1200IpmcSnoopingIgmpGroupAddressHardwareSwitch_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupAddressHardwareSwitch = _Me1200IpmcSnoopingIgmpGroupAddressHardwareSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 4, 1, 4),
    _Me1200IpmcSnoopingIgmpGroupAddressHardwareSwitch_Type()
)
me1200IpmcSnoopingIgmpGroupAddressHardwareSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupAddressHardwareSwitch.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListTable_Object = MibTable
me1200IpmcSnoopingIgmpGroupSrcListTable = _Me1200IpmcSnoopingIgmpGroupSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListTable.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListEntry_Object = MibTableRow
me1200IpmcSnoopingIgmpGroupSrcListEntry = _Me1200IpmcSnoopingIgmpGroupSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5, 1)
)
me1200IpmcSnoopingIgmpGroupSrcListEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupSrcListIfIndex"),
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupSrcListGroupAddress"),
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupSrcListPortIndex"),
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListEntry.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingIgmpGroupSrcListIfIndex_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupSrcListIfIndex = _Me1200IpmcSnoopingIgmpGroupSrcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5, 1, 1),
    _Me1200IpmcSnoopingIgmpGroupSrcListIfIndex_Type()
)
me1200IpmcSnoopingIgmpGroupSrcListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListIfIndex.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListGroupAddress_Type = IpAddress
_Me1200IpmcSnoopingIgmpGroupSrcListGroupAddress_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupSrcListGroupAddress = _Me1200IpmcSnoopingIgmpGroupSrcListGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5, 1, 2),
    _Me1200IpmcSnoopingIgmpGroupSrcListGroupAddress_Type()
)
me1200IpmcSnoopingIgmpGroupSrcListGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListGroupAddress.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListPortIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingIgmpGroupSrcListPortIndex_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupSrcListPortIndex = _Me1200IpmcSnoopingIgmpGroupSrcListPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5, 1, 3),
    _Me1200IpmcSnoopingIgmpGroupSrcListPortIndex_Type()
)
me1200IpmcSnoopingIgmpGroupSrcListPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListPortIndex.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListHostAddress_Type = IpAddress
_Me1200IpmcSnoopingIgmpGroupSrcListHostAddress_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupSrcListHostAddress = _Me1200IpmcSnoopingIgmpGroupSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5, 1, 4),
    _Me1200IpmcSnoopingIgmpGroupSrcListHostAddress_Type()
)
me1200IpmcSnoopingIgmpGroupSrcListHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListHostAddress.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListGroupFilterMode_Type = ME1200IpmcSnpIgmpGroupSrcListGroupFilterMode
_Me1200IpmcSnoopingIgmpGroupSrcListGroupFilterMode_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupSrcListGroupFilterMode = _Me1200IpmcSnoopingIgmpGroupSrcListGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5, 1, 5),
    _Me1200IpmcSnoopingIgmpGroupSrcListGroupFilterMode_Type()
)
me1200IpmcSnoopingIgmpGroupSrcListGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListGroupFilterMode.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListFilterTimer_Type = Unsigned32
_Me1200IpmcSnoopingIgmpGroupSrcListFilterTimer_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupSrcListFilterTimer = _Me1200IpmcSnoopingIgmpGroupSrcListFilterTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5, 1, 6),
    _Me1200IpmcSnoopingIgmpGroupSrcListFilterTimer_Type()
)
me1200IpmcSnoopingIgmpGroupSrcListFilterTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListFilterTimer.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListSourceType_Type = ME1200IpmcSnpIgmpGroupSrcListSourceType
_Me1200IpmcSnoopingIgmpGroupSrcListSourceType_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupSrcListSourceType = _Me1200IpmcSnoopingIgmpGroupSrcListSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5, 1, 7),
    _Me1200IpmcSnoopingIgmpGroupSrcListSourceType_Type()
)
me1200IpmcSnoopingIgmpGroupSrcListSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListSourceType.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListSourceTimer_Type = Unsigned32
_Me1200IpmcSnoopingIgmpGroupSrcListSourceTimer_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupSrcListSourceTimer = _Me1200IpmcSnoopingIgmpGroupSrcListSourceTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5, 1, 8),
    _Me1200IpmcSnoopingIgmpGroupSrcListSourceTimer_Type()
)
me1200IpmcSnoopingIgmpGroupSrcListSourceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListSourceTimer.setStatus("current")
_Me1200IpmcSnoopingIgmpGroupSrcListHardwareFilter_Type = TruthValue
_Me1200IpmcSnoopingIgmpGroupSrcListHardwareFilter_Object = MibTableColumn
me1200IpmcSnoopingIgmpGroupSrcListHardwareFilter = _Me1200IpmcSnoopingIgmpGroupSrcListHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 5, 1, 9),
    _Me1200IpmcSnoopingIgmpGroupSrcListHardwareFilter_Type()
)
me1200IpmcSnoopingIgmpGroupSrcListHardwareFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListHardwareFilter.setStatus("current")
_Me1200IpmcSnoopingMldRouterPortTable_Object = MibTable
me1200IpmcSnoopingMldRouterPortTable = _Me1200IpmcSnoopingMldRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 6)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldRouterPortTable.setStatus("current")
_Me1200IpmcSnoopingMldRouterPortEntry_Object = MibTableRow
me1200IpmcSnoopingMldRouterPortEntry = _Me1200IpmcSnoopingMldRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 6, 1)
)
me1200IpmcSnoopingMldRouterPortEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldRouterPortPortIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldRouterPortEntry.setStatus("current")
_Me1200IpmcSnoopingMldRouterPortPortIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingMldRouterPortPortIndex_Object = MibTableColumn
me1200IpmcSnoopingMldRouterPortPortIndex = _Me1200IpmcSnoopingMldRouterPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 6, 1, 1),
    _Me1200IpmcSnoopingMldRouterPortPortIndex_Type()
)
me1200IpmcSnoopingMldRouterPortPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldRouterPortPortIndex.setStatus("current")
_Me1200IpmcSnoopingMldRouterPortStatus_Type = ME1200IpmcSnpMldRouterPortStatus
_Me1200IpmcSnoopingMldRouterPortStatus_Object = MibTableColumn
me1200IpmcSnoopingMldRouterPortStatus = _Me1200IpmcSnoopingMldRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 6, 1, 2),
    _Me1200IpmcSnoopingMldRouterPortStatus_Type()
)
me1200IpmcSnoopingMldRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldRouterPortStatus.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusTable_Object = MibTable
me1200IpmcSnoopingMldVlanStatusTable = _Me1200IpmcSnoopingMldVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusTable.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusEntry_Object = MibTableRow
me1200IpmcSnoopingMldVlanStatusEntry = _Me1200IpmcSnoopingMldVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1)
)
me1200IpmcSnoopingMldVlanStatusEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusEntry.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingMldVlanStatusIfIndex_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusIfIndex = _Me1200IpmcSnoopingMldVlanStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 1),
    _Me1200IpmcSnoopingMldVlanStatusIfIndex_Type()
)
me1200IpmcSnoopingMldVlanStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusIfIndex.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusQuerierStatus_Type = ME1200IpmcSnpMldVlanStatusQuerierStatus
_Me1200IpmcSnoopingMldVlanStatusQuerierStatus_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusQuerierStatus = _Me1200IpmcSnoopingMldVlanStatusQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 2),
    _Me1200IpmcSnoopingMldVlanStatusQuerierStatus_Type()
)
me1200IpmcSnoopingMldVlanStatusQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusQuerierStatus.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusActiveQuerierAddress_Type = InetAddressIPv6
_Me1200IpmcSnoopingMldVlanStatusActiveQuerierAddress_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusActiveQuerierAddress = _Me1200IpmcSnoopingMldVlanStatusActiveQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 3),
    _Me1200IpmcSnoopingMldVlanStatusActiveQuerierAddress_Type()
)
me1200IpmcSnoopingMldVlanStatusActiveQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusActiveQuerierAddress.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusQuerierUptime_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusQuerierUptime_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusQuerierUptime = _Me1200IpmcSnoopingMldVlanStatusQuerierUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 4),
    _Me1200IpmcSnoopingMldVlanStatusQuerierUptime_Type()
)
me1200IpmcSnoopingMldVlanStatusQuerierUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusQuerierUptime.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusQueryInterval_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusQueryInterval_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusQueryInterval = _Me1200IpmcSnoopingMldVlanStatusQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 5),
    _Me1200IpmcSnoopingMldVlanStatusQueryInterval_Type()
)
me1200IpmcSnoopingMldVlanStatusQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusQueryInterval.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusStartupQueryCount_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusStartupQueryCount_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusStartupQueryCount = _Me1200IpmcSnoopingMldVlanStatusStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 6),
    _Me1200IpmcSnoopingMldVlanStatusStartupQueryCount_Type()
)
me1200IpmcSnoopingMldVlanStatusStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusStartupQueryCount.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusQuerierExpiryTime_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusQuerierExpiryTime_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusQuerierExpiryTime = _Me1200IpmcSnoopingMldVlanStatusQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 7),
    _Me1200IpmcSnoopingMldVlanStatusQuerierExpiryTime_Type()
)
me1200IpmcSnoopingMldVlanStatusQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusQuerierExpiryTime.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusQuerierVersion_Type = ME1200Unsigned8
_Me1200IpmcSnoopingMldVlanStatusQuerierVersion_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusQuerierVersion = _Me1200IpmcSnoopingMldVlanStatusQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 8),
    _Me1200IpmcSnoopingMldVlanStatusQuerierVersion_Type()
)
me1200IpmcSnoopingMldVlanStatusQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusQuerierVersion.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusQuerierPresentTimeout_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusQuerierPresentTimeout_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusQuerierPresentTimeout = _Me1200IpmcSnoopingMldVlanStatusQuerierPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 9),
    _Me1200IpmcSnoopingMldVlanStatusQuerierPresentTimeout_Type()
)
me1200IpmcSnoopingMldVlanStatusQuerierPresentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusQuerierPresentTimeout.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusHostVersion_Type = ME1200Unsigned8
_Me1200IpmcSnoopingMldVlanStatusHostVersion_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusHostVersion = _Me1200IpmcSnoopingMldVlanStatusHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 10),
    _Me1200IpmcSnoopingMldVlanStatusHostVersion_Type()
)
me1200IpmcSnoopingMldVlanStatusHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusHostVersion.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusHostPresentTimeout_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusHostPresentTimeout_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusHostPresentTimeout = _Me1200IpmcSnoopingMldVlanStatusHostPresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 11),
    _Me1200IpmcSnoopingMldVlanStatusHostPresentTimeout_Type()
)
me1200IpmcSnoopingMldVlanStatusHostPresentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusHostPresentTimeout.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusCounterTxQuery_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusCounterTxQuery_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusCounterTxQuery = _Me1200IpmcSnoopingMldVlanStatusCounterTxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 12),
    _Me1200IpmcSnoopingMldVlanStatusCounterTxQuery_Type()
)
me1200IpmcSnoopingMldVlanStatusCounterTxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusCounterTxQuery.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusCounterTxSpecificQuery_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusCounterTxSpecificQuery_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusCounterTxSpecificQuery = _Me1200IpmcSnoopingMldVlanStatusCounterTxSpecificQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 13),
    _Me1200IpmcSnoopingMldVlanStatusCounterTxSpecificQuery_Type()
)
me1200IpmcSnoopingMldVlanStatusCounterTxSpecificQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusCounterTxSpecificQuery.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusCounterRxQuery_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusCounterRxQuery_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusCounterRxQuery = _Me1200IpmcSnoopingMldVlanStatusCounterRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 14),
    _Me1200IpmcSnoopingMldVlanStatusCounterRxQuery_Type()
)
me1200IpmcSnoopingMldVlanStatusCounterRxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusCounterRxQuery.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusCounterRxV1Report_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusCounterRxV1Report_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusCounterRxV1Report = _Me1200IpmcSnoopingMldVlanStatusCounterRxV1Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 15),
    _Me1200IpmcSnoopingMldVlanStatusCounterRxV1Report_Type()
)
me1200IpmcSnoopingMldVlanStatusCounterRxV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusCounterRxV1Report.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusCounterRxV1Done_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusCounterRxV1Done_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusCounterRxV1Done = _Me1200IpmcSnoopingMldVlanStatusCounterRxV1Done_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 16),
    _Me1200IpmcSnoopingMldVlanStatusCounterRxV1Done_Type()
)
me1200IpmcSnoopingMldVlanStatusCounterRxV1Done.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusCounterRxV1Done.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusCounterRxV2Report_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusCounterRxV2Report_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusCounterRxV2Report = _Me1200IpmcSnoopingMldVlanStatusCounterRxV2Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 17),
    _Me1200IpmcSnoopingMldVlanStatusCounterRxV2Report_Type()
)
me1200IpmcSnoopingMldVlanStatusCounterRxV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusCounterRxV2Report.setStatus("current")
_Me1200IpmcSnoopingMldVlanStatusCounterRxErrors_Type = Unsigned32
_Me1200IpmcSnoopingMldVlanStatusCounterRxErrors_Object = MibTableColumn
me1200IpmcSnoopingMldVlanStatusCounterRxErrors = _Me1200IpmcSnoopingMldVlanStatusCounterRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 7, 1, 18),
    _Me1200IpmcSnoopingMldVlanStatusCounterRxErrors_Type()
)
me1200IpmcSnoopingMldVlanStatusCounterRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusCounterRxErrors.setStatus("current")
_Me1200IpmcSnoopingMldGroupAddressTable_Object = MibTable
me1200IpmcSnoopingMldGroupAddressTable = _Me1200IpmcSnoopingMldGroupAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 8)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupAddressTable.setStatus("current")
_Me1200IpmcSnoopingMldGroupAddressEntry_Object = MibTableRow
me1200IpmcSnoopingMldGroupAddressEntry = _Me1200IpmcSnoopingMldGroupAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 8, 1)
)
me1200IpmcSnoopingMldGroupAddressEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupAddressIfIndex"),
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupAddressGroupAddress"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupAddressEntry.setStatus("current")
_Me1200IpmcSnoopingMldGroupAddressIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingMldGroupAddressIfIndex_Object = MibTableColumn
me1200IpmcSnoopingMldGroupAddressIfIndex = _Me1200IpmcSnoopingMldGroupAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 8, 1, 1),
    _Me1200IpmcSnoopingMldGroupAddressIfIndex_Type()
)
me1200IpmcSnoopingMldGroupAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupAddressIfIndex.setStatus("current")
_Me1200IpmcSnoopingMldGroupAddressGroupAddress_Type = InetAddressIPv6
_Me1200IpmcSnoopingMldGroupAddressGroupAddress_Object = MibTableColumn
me1200IpmcSnoopingMldGroupAddressGroupAddress = _Me1200IpmcSnoopingMldGroupAddressGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 8, 1, 2),
    _Me1200IpmcSnoopingMldGroupAddressGroupAddress_Type()
)
me1200IpmcSnoopingMldGroupAddressGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupAddressGroupAddress.setStatus("current")
_Me1200IpmcSnoopingMldGroupAddressMemberPorts_Type = ME1200PortListStackable
_Me1200IpmcSnoopingMldGroupAddressMemberPorts_Object = MibTableColumn
me1200IpmcSnoopingMldGroupAddressMemberPorts = _Me1200IpmcSnoopingMldGroupAddressMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 8, 1, 3),
    _Me1200IpmcSnoopingMldGroupAddressMemberPorts_Type()
)
me1200IpmcSnoopingMldGroupAddressMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupAddressMemberPorts.setStatus("current")
_Me1200IpmcSnoopingMldGroupAddressHardwareSwitch_Type = TruthValue
_Me1200IpmcSnoopingMldGroupAddressHardwareSwitch_Object = MibTableColumn
me1200IpmcSnoopingMldGroupAddressHardwareSwitch = _Me1200IpmcSnoopingMldGroupAddressHardwareSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 8, 1, 4),
    _Me1200IpmcSnoopingMldGroupAddressHardwareSwitch_Type()
)
me1200IpmcSnoopingMldGroupAddressHardwareSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupAddressHardwareSwitch.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListTable_Object = MibTable
me1200IpmcSnoopingMldGroupSrcListTable = _Me1200IpmcSnoopingMldGroupSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9)
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListTable.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListEntry_Object = MibTableRow
me1200IpmcSnoopingMldGroupSrcListEntry = _Me1200IpmcSnoopingMldGroupSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9, 1)
)
me1200IpmcSnoopingMldGroupSrcListEntry.setIndexNames(
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupSrcListIfIndex"),
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupSrcListGroupAddress"),
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupSrcListPortIndex"),
    (0, "ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListEntry.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingMldGroupSrcListIfIndex_Object = MibTableColumn
me1200IpmcSnoopingMldGroupSrcListIfIndex = _Me1200IpmcSnoopingMldGroupSrcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9, 1, 1),
    _Me1200IpmcSnoopingMldGroupSrcListIfIndex_Type()
)
me1200IpmcSnoopingMldGroupSrcListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListIfIndex.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListGroupAddress_Type = InetAddressIPv6
_Me1200IpmcSnoopingMldGroupSrcListGroupAddress_Object = MibTableColumn
me1200IpmcSnoopingMldGroupSrcListGroupAddress = _Me1200IpmcSnoopingMldGroupSrcListGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9, 1, 2),
    _Me1200IpmcSnoopingMldGroupSrcListGroupAddress_Type()
)
me1200IpmcSnoopingMldGroupSrcListGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListGroupAddress.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListPortIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingMldGroupSrcListPortIndex_Object = MibTableColumn
me1200IpmcSnoopingMldGroupSrcListPortIndex = _Me1200IpmcSnoopingMldGroupSrcListPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9, 1, 3),
    _Me1200IpmcSnoopingMldGroupSrcListPortIndex_Type()
)
me1200IpmcSnoopingMldGroupSrcListPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListPortIndex.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListHostAddress_Type = InetAddressIPv6
_Me1200IpmcSnoopingMldGroupSrcListHostAddress_Object = MibTableColumn
me1200IpmcSnoopingMldGroupSrcListHostAddress = _Me1200IpmcSnoopingMldGroupSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9, 1, 4),
    _Me1200IpmcSnoopingMldGroupSrcListHostAddress_Type()
)
me1200IpmcSnoopingMldGroupSrcListHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListHostAddress.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListGroupFilterMode_Type = ME1200IpmcSnpMldGroupSrcListGroupFilterMode
_Me1200IpmcSnoopingMldGroupSrcListGroupFilterMode_Object = MibTableColumn
me1200IpmcSnoopingMldGroupSrcListGroupFilterMode = _Me1200IpmcSnoopingMldGroupSrcListGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9, 1, 5),
    _Me1200IpmcSnoopingMldGroupSrcListGroupFilterMode_Type()
)
me1200IpmcSnoopingMldGroupSrcListGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListGroupFilterMode.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListFilterTimer_Type = Unsigned32
_Me1200IpmcSnoopingMldGroupSrcListFilterTimer_Object = MibTableColumn
me1200IpmcSnoopingMldGroupSrcListFilterTimer = _Me1200IpmcSnoopingMldGroupSrcListFilterTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9, 1, 6),
    _Me1200IpmcSnoopingMldGroupSrcListFilterTimer_Type()
)
me1200IpmcSnoopingMldGroupSrcListFilterTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListFilterTimer.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListSourceType_Type = ME1200IpmcSnpMldGroupSrcListSourceType
_Me1200IpmcSnoopingMldGroupSrcListSourceType_Object = MibTableColumn
me1200IpmcSnoopingMldGroupSrcListSourceType = _Me1200IpmcSnoopingMldGroupSrcListSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9, 1, 7),
    _Me1200IpmcSnoopingMldGroupSrcListSourceType_Type()
)
me1200IpmcSnoopingMldGroupSrcListSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListSourceType.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListSourceTimer_Type = Unsigned32
_Me1200IpmcSnoopingMldGroupSrcListSourceTimer_Object = MibTableColumn
me1200IpmcSnoopingMldGroupSrcListSourceTimer = _Me1200IpmcSnoopingMldGroupSrcListSourceTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9, 1, 8),
    _Me1200IpmcSnoopingMldGroupSrcListSourceTimer_Type()
)
me1200IpmcSnoopingMldGroupSrcListSourceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListSourceTimer.setStatus("current")
_Me1200IpmcSnoopingMldGroupSrcListHardwareFilter_Type = TruthValue
_Me1200IpmcSnoopingMldGroupSrcListHardwareFilter_Object = MibTableColumn
me1200IpmcSnoopingMldGroupSrcListHardwareFilter = _Me1200IpmcSnoopingMldGroupSrcListHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 3, 9, 1, 9),
    _Me1200IpmcSnoopingMldGroupSrcListHardwareFilter_Type()
)
me1200IpmcSnoopingMldGroupSrcListHardwareFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListHardwareFilter.setStatus("current")
_Me1200IpmcSnoopingControl_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingControl = _Me1200IpmcSnoopingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 4)
)
_Me1200IpmcSnoopingControlStatistics_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingControlStatistics = _Me1200IpmcSnoopingControlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 4, 1)
)
_Me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndex_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndex = _Me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 4, 1, 1)
)
_Me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex_Object = MibScalar
me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex = _Me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 4, 1, 1, 1),
    _Me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex_Type()
)
me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex.setStatus("current")
_Me1200IpmcSnoopingControlStatisticsMldClearByIfIndex_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingControlStatisticsMldClearByIfIndex = _Me1200IpmcSnoopingControlStatisticsMldClearByIfIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 4, 1, 2)
)
_Me1200IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex_Object = MibScalar
me1200IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex = _Me1200IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 1, 4, 1, 2, 1),
    _Me1200IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex_Type()
)
me1200IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex.setStatus("current")
_Me1200IpmcSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingMIBConformance = _Me1200IpmcSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2)
)
_Me1200IpmcSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingMIBCompliances = _Me1200IpmcSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 1)
)
_Me1200IpmcSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
me1200IpmcSnoopingMIBGroups = _Me1200IpmcSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2)
)

# Managed Objects groups

me1200IpmcSnoopingIgmpGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 1)
)
me1200IpmcSnoopingIgmpGlobalsInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGlobalsAdminState"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGlobalsUnregisteredFlooding"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGlobalsSsmRangeAddress"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGlobalsSsmRangeMask"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGlobalsProxy"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGlobalsLeaveProxy"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGlobalsInfoGroup.setStatus("current")

me1200IpmcSnoopingIgmpPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 2)
)
me1200IpmcSnoopingIgmpPortTableInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpPortAsRouterPort"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpPortDoFastLeave"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpPortThrottlingNumber"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpPortFilteringProfile"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpPortTableInfoGroup.setStatus("current")

me1200IpmcSnoopingIgmpInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 3)
)
me1200IpmcSnoopingIgmpInterfaceTableInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceAdminState"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceQuerierElection"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceQuerierAddress"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceCompatibility"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfacePriority"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceRv"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceQi"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceQri"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceLmqi"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceUri"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableInfoGroup.setStatus("current")

me1200IpmcSnoopingIgmpInterfaceTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 4)
)
me1200IpmcSnoopingIgmpInterfaceTableRowEditorInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorIfIndex"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorAdminState"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierElection"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierAddress"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorCompatibility"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorPriority"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorRv"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorQi"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorQri"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorLmqi"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorUri"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpInterfaceTableRowEditorInfoGroup.setStatus("current")

me1200IpmcSnoopingMldGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 5)
)
me1200IpmcSnoopingMldGlobalsInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGlobalsAdminState"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGlobalsUnregisteredFlooding"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGlobalsSsmRangeAddress"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGlobalsSsmRangeMask"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGlobalsProxy"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGlobalsLeaveProxy"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGlobalsInfoGroup.setStatus("current")

me1200IpmcSnoopingMldPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 6)
)
me1200IpmcSnoopingMldPortTableInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldPortAsRouterPort"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldPortDoFastLeave"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldPortThrottlingNumber"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldPortFilteringProfile"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldPortTableInfoGroup.setStatus("current")

me1200IpmcSnoopingMldInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 7)
)
me1200IpmcSnoopingMldInterfaceTableInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceAdminState"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceQuerierElection"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceCompatibility"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfacePriority"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceRv"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceQi"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceQri"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceLlqi"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceUri"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableInfoGroup.setStatus("current")

me1200IpmcSnoopingMldInterfaceTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 8)
)
me1200IpmcSnoopingMldInterfaceTableRowEditorInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorIfIndex"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorAdminState"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorQuerierElection"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorCompatibility"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorPriority"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorRv"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorQi"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorQri"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorLlqi"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorUri"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldInterfaceTableRowEditorInfoGroup.setStatus("current")

me1200IpmcSnoopingGroupAddressCountInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 9)
)
me1200IpmcSnoopingGroupAddressCountInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingGroupAddressCountFromIgmp"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingGroupAddressCountFromMld"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingGroupAddressCountInfoGroup.setStatus("current")

me1200IpmcSnoopingIgmpRouterPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 10)
)
me1200IpmcSnoopingIgmpRouterPortTableInfoGroup.setObjects(
    ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpRouterPortStatus")
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpRouterPortTableInfoGroup.setStatus("current")

me1200IpmcSnoopingIgmpVlanStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 11)
)
me1200IpmcSnoopingIgmpVlanStatusTableInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusQuerierStatus"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusActiveQuerierAddress"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusQuerierUptime"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusQueryInterval"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusStartupQueryCount"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusQuerierExpiryTime"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusQuerierVersion"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusQuerierPresentTimeout"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusHostVersion"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusHostPresentTimeout"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusCounterTxQuery"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusCounterTxSpecificQuery"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusCounterRxQuery"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusCounterRxV1Join"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Join"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Leave"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusCounterRxV3Join"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusCounterRxErrors"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpVlanStatusTableInfoGroup.setStatus("current")

me1200IpmcSnoopingIgmpGroupAddressTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 12)
)
me1200IpmcSnoopingIgmpGroupAddressTableInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupAddressMemberPorts"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupAddressHardwareSwitch"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupAddressTableInfoGroup.setStatus("current")

me1200IpmcSnoopingIgmpGroupSrcListTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 13)
)
me1200IpmcSnoopingIgmpGroupSrcListTableInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupSrcListGroupFilterMode"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupSrcListFilterTimer"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupSrcListSourceType"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupSrcListSourceTimer"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupSrcListHardwareFilter"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingIgmpGroupSrcListTableInfoGroup.setStatus("current")

me1200IpmcSnoopingMldRouterPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 14)
)
me1200IpmcSnoopingMldRouterPortTableInfoGroup.setObjects(
    ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldRouterPortStatus")
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldRouterPortTableInfoGroup.setStatus("current")

me1200IpmcSnoopingMldVlanStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 15)
)
me1200IpmcSnoopingMldVlanStatusTableInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusQuerierStatus"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusActiveQuerierAddress"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusQuerierUptime"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusQueryInterval"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusStartupQueryCount"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusQuerierExpiryTime"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusQuerierVersion"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusQuerierPresentTimeout"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusHostVersion"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusHostPresentTimeout"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusCounterTxQuery"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusCounterTxSpecificQuery"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusCounterRxQuery"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusCounterRxV1Report"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusCounterRxV1Done"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusCounterRxV2Report"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusCounterRxErrors"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldVlanStatusTableInfoGroup.setStatus("current")

me1200IpmcSnoopingMldGroupAddressTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 16)
)
me1200IpmcSnoopingMldGroupAddressTableInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupAddressMemberPorts"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupAddressHardwareSwitch"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupAddressTableInfoGroup.setStatus("current")

me1200IpmcSnoopingMldGroupSrcListTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 17)
)
me1200IpmcSnoopingMldGroupSrcListTableInfoGroup.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupSrcListGroupFilterMode"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupSrcListFilterTimer"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupSrcListSourceType"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupSrcListSourceTimer"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupSrcListHardwareFilter"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMldGroupSrcListTableInfoGroup.setStatus("current")

me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 18)
)
me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup.setObjects(
    ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex")
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup.setStatus("current")

me1200IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 2, 19)
)
me1200IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup.setObjects(
    ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex")
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200IpmcSnoopingMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 69, 2, 1, 1)
)
me1200IpmcSnoopingMibCompliance.setObjects(
      *(("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGlobalsInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpPortTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpInterfaceTableRowEditorInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGlobalsInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldPortTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldInterfaceTableRowEditorInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingGroupAddressCountInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpRouterPortTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpVlanStatusTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupAddressTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingIgmpGroupSrcListTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldRouterPortTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldVlanStatusTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupAddressTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingMldGroupSrcListTableInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup"),
        ("ME1200-IPMC-SNOOPING-MIB", "me1200IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200IpmcSnoopingMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-IPMC-SNOOPING-MIB",
    **{"ME1200IpmcSnpIgmpInterfaceCompatibility": ME1200IpmcSnpIgmpInterfaceCompatibility,
       "ME1200IpmcSnpMldInterfaceCompatibility": ME1200IpmcSnpMldInterfaceCompatibility,
       "ME1200IpmcSnpIgmpRouterPortStatus": ME1200IpmcSnpIgmpRouterPortStatus,
       "ME1200IpmcSnpIgmpVlanStatusQuerierStatus": ME1200IpmcSnpIgmpVlanStatusQuerierStatus,
       "ME1200IpmcSnpIgmpGroupSrcListGroupFilterMode": ME1200IpmcSnpIgmpGroupSrcListGroupFilterMode,
       "ME1200IpmcSnpIgmpGroupSrcListSourceType": ME1200IpmcSnpIgmpGroupSrcListSourceType,
       "ME1200IpmcSnpMldRouterPortStatus": ME1200IpmcSnpMldRouterPortStatus,
       "ME1200IpmcSnpMldVlanStatusQuerierStatus": ME1200IpmcSnpMldVlanStatusQuerierStatus,
       "ME1200IpmcSnpMldGroupSrcListGroupFilterMode": ME1200IpmcSnpMldGroupSrcListGroupFilterMode,
       "ME1200IpmcSnpMldGroupSrcListSourceType": ME1200IpmcSnpMldGroupSrcListSourceType,
       "me1200IpmcSnoopingMib": me1200IpmcSnoopingMib,
       "me1200IpmcSnoopingMIBObjects": me1200IpmcSnoopingMIBObjects,
       "me1200IpmcSnoopingConfig": me1200IpmcSnoopingConfig,
       "me1200IpmcSnoopingIgmpGlobals": me1200IpmcSnoopingIgmpGlobals,
       "me1200IpmcSnoopingIgmpGlobalsAdminState": me1200IpmcSnoopingIgmpGlobalsAdminState,
       "me1200IpmcSnoopingIgmpGlobalsUnregisteredFlooding": me1200IpmcSnoopingIgmpGlobalsUnregisteredFlooding,
       "me1200IpmcSnoopingIgmpGlobalsSsmRangeAddress": me1200IpmcSnoopingIgmpGlobalsSsmRangeAddress,
       "me1200IpmcSnoopingIgmpGlobalsSsmRangeMask": me1200IpmcSnoopingIgmpGlobalsSsmRangeMask,
       "me1200IpmcSnoopingIgmpGlobalsProxy": me1200IpmcSnoopingIgmpGlobalsProxy,
       "me1200IpmcSnoopingIgmpGlobalsLeaveProxy": me1200IpmcSnoopingIgmpGlobalsLeaveProxy,
       "me1200IpmcSnoopingIgmpPortTable": me1200IpmcSnoopingIgmpPortTable,
       "me1200IpmcSnoopingIgmpPortEntry": me1200IpmcSnoopingIgmpPortEntry,
       "me1200IpmcSnoopingIgmpPortPortIndex": me1200IpmcSnoopingIgmpPortPortIndex,
       "me1200IpmcSnoopingIgmpPortAsRouterPort": me1200IpmcSnoopingIgmpPortAsRouterPort,
       "me1200IpmcSnoopingIgmpPortDoFastLeave": me1200IpmcSnoopingIgmpPortDoFastLeave,
       "me1200IpmcSnoopingIgmpPortThrottlingNumber": me1200IpmcSnoopingIgmpPortThrottlingNumber,
       "me1200IpmcSnoopingIgmpPortFilteringProfile": me1200IpmcSnoopingIgmpPortFilteringProfile,
       "me1200IpmcSnoopingIgmpInterfaceTable": me1200IpmcSnoopingIgmpInterfaceTable,
       "me1200IpmcSnoopingIgmpInterfaceEntry": me1200IpmcSnoopingIgmpInterfaceEntry,
       "me1200IpmcSnoopingIgmpInterfaceIfIndex": me1200IpmcSnoopingIgmpInterfaceIfIndex,
       "me1200IpmcSnoopingIgmpInterfaceAdminState": me1200IpmcSnoopingIgmpInterfaceAdminState,
       "me1200IpmcSnoopingIgmpInterfaceQuerierElection": me1200IpmcSnoopingIgmpInterfaceQuerierElection,
       "me1200IpmcSnoopingIgmpInterfaceQuerierAddress": me1200IpmcSnoopingIgmpInterfaceQuerierAddress,
       "me1200IpmcSnoopingIgmpInterfaceCompatibility": me1200IpmcSnoopingIgmpInterfaceCompatibility,
       "me1200IpmcSnoopingIgmpInterfacePriority": me1200IpmcSnoopingIgmpInterfacePriority,
       "me1200IpmcSnoopingIgmpInterfaceRv": me1200IpmcSnoopingIgmpInterfaceRv,
       "me1200IpmcSnoopingIgmpInterfaceQi": me1200IpmcSnoopingIgmpInterfaceQi,
       "me1200IpmcSnoopingIgmpInterfaceQri": me1200IpmcSnoopingIgmpInterfaceQri,
       "me1200IpmcSnoopingIgmpInterfaceLmqi": me1200IpmcSnoopingIgmpInterfaceLmqi,
       "me1200IpmcSnoopingIgmpInterfaceUri": me1200IpmcSnoopingIgmpInterfaceUri,
       "me1200IpmcSnoopingIgmpInterfaceAction": me1200IpmcSnoopingIgmpInterfaceAction,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditor": me1200IpmcSnoopingIgmpInterfaceTableRowEditor,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorIfIndex": me1200IpmcSnoopingIgmpInterfaceTableRowEditorIfIndex,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorAdminState": me1200IpmcSnoopingIgmpInterfaceTableRowEditorAdminState,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierElection": me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierElection,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierAddress": me1200IpmcSnoopingIgmpInterfaceTableRowEditorQuerierAddress,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorCompatibility": me1200IpmcSnoopingIgmpInterfaceTableRowEditorCompatibility,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorPriority": me1200IpmcSnoopingIgmpInterfaceTableRowEditorPriority,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorRv": me1200IpmcSnoopingIgmpInterfaceTableRowEditorRv,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorQi": me1200IpmcSnoopingIgmpInterfaceTableRowEditorQi,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorQri": me1200IpmcSnoopingIgmpInterfaceTableRowEditorQri,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorLmqi": me1200IpmcSnoopingIgmpInterfaceTableRowEditorLmqi,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorUri": me1200IpmcSnoopingIgmpInterfaceTableRowEditorUri,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorAction": me1200IpmcSnoopingIgmpInterfaceTableRowEditorAction,
       "me1200IpmcSnoopingMldGlobals": me1200IpmcSnoopingMldGlobals,
       "me1200IpmcSnoopingMldGlobalsAdminState": me1200IpmcSnoopingMldGlobalsAdminState,
       "me1200IpmcSnoopingMldGlobalsUnregisteredFlooding": me1200IpmcSnoopingMldGlobalsUnregisteredFlooding,
       "me1200IpmcSnoopingMldGlobalsSsmRangeAddress": me1200IpmcSnoopingMldGlobalsSsmRangeAddress,
       "me1200IpmcSnoopingMldGlobalsSsmRangeMask": me1200IpmcSnoopingMldGlobalsSsmRangeMask,
       "me1200IpmcSnoopingMldGlobalsProxy": me1200IpmcSnoopingMldGlobalsProxy,
       "me1200IpmcSnoopingMldGlobalsLeaveProxy": me1200IpmcSnoopingMldGlobalsLeaveProxy,
       "me1200IpmcSnoopingMldPortTable": me1200IpmcSnoopingMldPortTable,
       "me1200IpmcSnoopingMldPortEntry": me1200IpmcSnoopingMldPortEntry,
       "me1200IpmcSnoopingMldPortPortIndex": me1200IpmcSnoopingMldPortPortIndex,
       "me1200IpmcSnoopingMldPortAsRouterPort": me1200IpmcSnoopingMldPortAsRouterPort,
       "me1200IpmcSnoopingMldPortDoFastLeave": me1200IpmcSnoopingMldPortDoFastLeave,
       "me1200IpmcSnoopingMldPortThrottlingNumber": me1200IpmcSnoopingMldPortThrottlingNumber,
       "me1200IpmcSnoopingMldPortFilteringProfile": me1200IpmcSnoopingMldPortFilteringProfile,
       "me1200IpmcSnoopingMldInterfaceTable": me1200IpmcSnoopingMldInterfaceTable,
       "me1200IpmcSnoopingMldInterfaceEntry": me1200IpmcSnoopingMldInterfaceEntry,
       "me1200IpmcSnoopingMldInterfaceIfIndex": me1200IpmcSnoopingMldInterfaceIfIndex,
       "me1200IpmcSnoopingMldInterfaceAdminState": me1200IpmcSnoopingMldInterfaceAdminState,
       "me1200IpmcSnoopingMldInterfaceQuerierElection": me1200IpmcSnoopingMldInterfaceQuerierElection,
       "me1200IpmcSnoopingMldInterfaceCompatibility": me1200IpmcSnoopingMldInterfaceCompatibility,
       "me1200IpmcSnoopingMldInterfacePriority": me1200IpmcSnoopingMldInterfacePriority,
       "me1200IpmcSnoopingMldInterfaceRv": me1200IpmcSnoopingMldInterfaceRv,
       "me1200IpmcSnoopingMldInterfaceQi": me1200IpmcSnoopingMldInterfaceQi,
       "me1200IpmcSnoopingMldInterfaceQri": me1200IpmcSnoopingMldInterfaceQri,
       "me1200IpmcSnoopingMldInterfaceLlqi": me1200IpmcSnoopingMldInterfaceLlqi,
       "me1200IpmcSnoopingMldInterfaceUri": me1200IpmcSnoopingMldInterfaceUri,
       "me1200IpmcSnoopingMldInterfaceAction": me1200IpmcSnoopingMldInterfaceAction,
       "me1200IpmcSnoopingMldInterfaceTableRowEditor": me1200IpmcSnoopingMldInterfaceTableRowEditor,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorIfIndex": me1200IpmcSnoopingMldInterfaceTableRowEditorIfIndex,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorAdminState": me1200IpmcSnoopingMldInterfaceTableRowEditorAdminState,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorQuerierElection": me1200IpmcSnoopingMldInterfaceTableRowEditorQuerierElection,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorCompatibility": me1200IpmcSnoopingMldInterfaceTableRowEditorCompatibility,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorPriority": me1200IpmcSnoopingMldInterfaceTableRowEditorPriority,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorRv": me1200IpmcSnoopingMldInterfaceTableRowEditorRv,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorQi": me1200IpmcSnoopingMldInterfaceTableRowEditorQi,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorQri": me1200IpmcSnoopingMldInterfaceTableRowEditorQri,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorLlqi": me1200IpmcSnoopingMldInterfaceTableRowEditorLlqi,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorUri": me1200IpmcSnoopingMldInterfaceTableRowEditorUri,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorAction": me1200IpmcSnoopingMldInterfaceTableRowEditorAction,
       "me1200IpmcSnoopingStatus": me1200IpmcSnoopingStatus,
       "me1200IpmcSnoopingGroupAddressCount": me1200IpmcSnoopingGroupAddressCount,
       "me1200IpmcSnoopingGroupAddressCountFromIgmp": me1200IpmcSnoopingGroupAddressCountFromIgmp,
       "me1200IpmcSnoopingGroupAddressCountFromMld": me1200IpmcSnoopingGroupAddressCountFromMld,
       "me1200IpmcSnoopingIgmpRouterPortTable": me1200IpmcSnoopingIgmpRouterPortTable,
       "me1200IpmcSnoopingIgmpRouterPortEntry": me1200IpmcSnoopingIgmpRouterPortEntry,
       "me1200IpmcSnoopingIgmpRouterPortPortIndex": me1200IpmcSnoopingIgmpRouterPortPortIndex,
       "me1200IpmcSnoopingIgmpRouterPortStatus": me1200IpmcSnoopingIgmpRouterPortStatus,
       "me1200IpmcSnoopingIgmpVlanStatusTable": me1200IpmcSnoopingIgmpVlanStatusTable,
       "me1200IpmcSnoopingIgmpVlanStatusEntry": me1200IpmcSnoopingIgmpVlanStatusEntry,
       "me1200IpmcSnoopingIgmpVlanStatusIfIndex": me1200IpmcSnoopingIgmpVlanStatusIfIndex,
       "me1200IpmcSnoopingIgmpVlanStatusQuerierStatus": me1200IpmcSnoopingIgmpVlanStatusQuerierStatus,
       "me1200IpmcSnoopingIgmpVlanStatusActiveQuerierAddress": me1200IpmcSnoopingIgmpVlanStatusActiveQuerierAddress,
       "me1200IpmcSnoopingIgmpVlanStatusQuerierUptime": me1200IpmcSnoopingIgmpVlanStatusQuerierUptime,
       "me1200IpmcSnoopingIgmpVlanStatusQueryInterval": me1200IpmcSnoopingIgmpVlanStatusQueryInterval,
       "me1200IpmcSnoopingIgmpVlanStatusStartupQueryCount": me1200IpmcSnoopingIgmpVlanStatusStartupQueryCount,
       "me1200IpmcSnoopingIgmpVlanStatusQuerierExpiryTime": me1200IpmcSnoopingIgmpVlanStatusQuerierExpiryTime,
       "me1200IpmcSnoopingIgmpVlanStatusQuerierVersion": me1200IpmcSnoopingIgmpVlanStatusQuerierVersion,
       "me1200IpmcSnoopingIgmpVlanStatusQuerierPresentTimeout": me1200IpmcSnoopingIgmpVlanStatusQuerierPresentTimeout,
       "me1200IpmcSnoopingIgmpVlanStatusHostVersion": me1200IpmcSnoopingIgmpVlanStatusHostVersion,
       "me1200IpmcSnoopingIgmpVlanStatusHostPresentTimeout": me1200IpmcSnoopingIgmpVlanStatusHostPresentTimeout,
       "me1200IpmcSnoopingIgmpVlanStatusCounterTxQuery": me1200IpmcSnoopingIgmpVlanStatusCounterTxQuery,
       "me1200IpmcSnoopingIgmpVlanStatusCounterTxSpecificQuery": me1200IpmcSnoopingIgmpVlanStatusCounterTxSpecificQuery,
       "me1200IpmcSnoopingIgmpVlanStatusCounterRxQuery": me1200IpmcSnoopingIgmpVlanStatusCounterRxQuery,
       "me1200IpmcSnoopingIgmpVlanStatusCounterRxV1Join": me1200IpmcSnoopingIgmpVlanStatusCounterRxV1Join,
       "me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Join": me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Join,
       "me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Leave": me1200IpmcSnoopingIgmpVlanStatusCounterRxV2Leave,
       "me1200IpmcSnoopingIgmpVlanStatusCounterRxV3Join": me1200IpmcSnoopingIgmpVlanStatusCounterRxV3Join,
       "me1200IpmcSnoopingIgmpVlanStatusCounterRxErrors": me1200IpmcSnoopingIgmpVlanStatusCounterRxErrors,
       "me1200IpmcSnoopingIgmpGroupAddressTable": me1200IpmcSnoopingIgmpGroupAddressTable,
       "me1200IpmcSnoopingIgmpGroupAddressEntry": me1200IpmcSnoopingIgmpGroupAddressEntry,
       "me1200IpmcSnoopingIgmpGroupAddressIfIndex": me1200IpmcSnoopingIgmpGroupAddressIfIndex,
       "me1200IpmcSnoopingIgmpGroupAddressGroupAddress": me1200IpmcSnoopingIgmpGroupAddressGroupAddress,
       "me1200IpmcSnoopingIgmpGroupAddressMemberPorts": me1200IpmcSnoopingIgmpGroupAddressMemberPorts,
       "me1200IpmcSnoopingIgmpGroupAddressHardwareSwitch": me1200IpmcSnoopingIgmpGroupAddressHardwareSwitch,
       "me1200IpmcSnoopingIgmpGroupSrcListTable": me1200IpmcSnoopingIgmpGroupSrcListTable,
       "me1200IpmcSnoopingIgmpGroupSrcListEntry": me1200IpmcSnoopingIgmpGroupSrcListEntry,
       "me1200IpmcSnoopingIgmpGroupSrcListIfIndex": me1200IpmcSnoopingIgmpGroupSrcListIfIndex,
       "me1200IpmcSnoopingIgmpGroupSrcListGroupAddress": me1200IpmcSnoopingIgmpGroupSrcListGroupAddress,
       "me1200IpmcSnoopingIgmpGroupSrcListPortIndex": me1200IpmcSnoopingIgmpGroupSrcListPortIndex,
       "me1200IpmcSnoopingIgmpGroupSrcListHostAddress": me1200IpmcSnoopingIgmpGroupSrcListHostAddress,
       "me1200IpmcSnoopingIgmpGroupSrcListGroupFilterMode": me1200IpmcSnoopingIgmpGroupSrcListGroupFilterMode,
       "me1200IpmcSnoopingIgmpGroupSrcListFilterTimer": me1200IpmcSnoopingIgmpGroupSrcListFilterTimer,
       "me1200IpmcSnoopingIgmpGroupSrcListSourceType": me1200IpmcSnoopingIgmpGroupSrcListSourceType,
       "me1200IpmcSnoopingIgmpGroupSrcListSourceTimer": me1200IpmcSnoopingIgmpGroupSrcListSourceTimer,
       "me1200IpmcSnoopingIgmpGroupSrcListHardwareFilter": me1200IpmcSnoopingIgmpGroupSrcListHardwareFilter,
       "me1200IpmcSnoopingMldRouterPortTable": me1200IpmcSnoopingMldRouterPortTable,
       "me1200IpmcSnoopingMldRouterPortEntry": me1200IpmcSnoopingMldRouterPortEntry,
       "me1200IpmcSnoopingMldRouterPortPortIndex": me1200IpmcSnoopingMldRouterPortPortIndex,
       "me1200IpmcSnoopingMldRouterPortStatus": me1200IpmcSnoopingMldRouterPortStatus,
       "me1200IpmcSnoopingMldVlanStatusTable": me1200IpmcSnoopingMldVlanStatusTable,
       "me1200IpmcSnoopingMldVlanStatusEntry": me1200IpmcSnoopingMldVlanStatusEntry,
       "me1200IpmcSnoopingMldVlanStatusIfIndex": me1200IpmcSnoopingMldVlanStatusIfIndex,
       "me1200IpmcSnoopingMldVlanStatusQuerierStatus": me1200IpmcSnoopingMldVlanStatusQuerierStatus,
       "me1200IpmcSnoopingMldVlanStatusActiveQuerierAddress": me1200IpmcSnoopingMldVlanStatusActiveQuerierAddress,
       "me1200IpmcSnoopingMldVlanStatusQuerierUptime": me1200IpmcSnoopingMldVlanStatusQuerierUptime,
       "me1200IpmcSnoopingMldVlanStatusQueryInterval": me1200IpmcSnoopingMldVlanStatusQueryInterval,
       "me1200IpmcSnoopingMldVlanStatusStartupQueryCount": me1200IpmcSnoopingMldVlanStatusStartupQueryCount,
       "me1200IpmcSnoopingMldVlanStatusQuerierExpiryTime": me1200IpmcSnoopingMldVlanStatusQuerierExpiryTime,
       "me1200IpmcSnoopingMldVlanStatusQuerierVersion": me1200IpmcSnoopingMldVlanStatusQuerierVersion,
       "me1200IpmcSnoopingMldVlanStatusQuerierPresentTimeout": me1200IpmcSnoopingMldVlanStatusQuerierPresentTimeout,
       "me1200IpmcSnoopingMldVlanStatusHostVersion": me1200IpmcSnoopingMldVlanStatusHostVersion,
       "me1200IpmcSnoopingMldVlanStatusHostPresentTimeout": me1200IpmcSnoopingMldVlanStatusHostPresentTimeout,
       "me1200IpmcSnoopingMldVlanStatusCounterTxQuery": me1200IpmcSnoopingMldVlanStatusCounterTxQuery,
       "me1200IpmcSnoopingMldVlanStatusCounterTxSpecificQuery": me1200IpmcSnoopingMldVlanStatusCounterTxSpecificQuery,
       "me1200IpmcSnoopingMldVlanStatusCounterRxQuery": me1200IpmcSnoopingMldVlanStatusCounterRxQuery,
       "me1200IpmcSnoopingMldVlanStatusCounterRxV1Report": me1200IpmcSnoopingMldVlanStatusCounterRxV1Report,
       "me1200IpmcSnoopingMldVlanStatusCounterRxV1Done": me1200IpmcSnoopingMldVlanStatusCounterRxV1Done,
       "me1200IpmcSnoopingMldVlanStatusCounterRxV2Report": me1200IpmcSnoopingMldVlanStatusCounterRxV2Report,
       "me1200IpmcSnoopingMldVlanStatusCounterRxErrors": me1200IpmcSnoopingMldVlanStatusCounterRxErrors,
       "me1200IpmcSnoopingMldGroupAddressTable": me1200IpmcSnoopingMldGroupAddressTable,
       "me1200IpmcSnoopingMldGroupAddressEntry": me1200IpmcSnoopingMldGroupAddressEntry,
       "me1200IpmcSnoopingMldGroupAddressIfIndex": me1200IpmcSnoopingMldGroupAddressIfIndex,
       "me1200IpmcSnoopingMldGroupAddressGroupAddress": me1200IpmcSnoopingMldGroupAddressGroupAddress,
       "me1200IpmcSnoopingMldGroupAddressMemberPorts": me1200IpmcSnoopingMldGroupAddressMemberPorts,
       "me1200IpmcSnoopingMldGroupAddressHardwareSwitch": me1200IpmcSnoopingMldGroupAddressHardwareSwitch,
       "me1200IpmcSnoopingMldGroupSrcListTable": me1200IpmcSnoopingMldGroupSrcListTable,
       "me1200IpmcSnoopingMldGroupSrcListEntry": me1200IpmcSnoopingMldGroupSrcListEntry,
       "me1200IpmcSnoopingMldGroupSrcListIfIndex": me1200IpmcSnoopingMldGroupSrcListIfIndex,
       "me1200IpmcSnoopingMldGroupSrcListGroupAddress": me1200IpmcSnoopingMldGroupSrcListGroupAddress,
       "me1200IpmcSnoopingMldGroupSrcListPortIndex": me1200IpmcSnoopingMldGroupSrcListPortIndex,
       "me1200IpmcSnoopingMldGroupSrcListHostAddress": me1200IpmcSnoopingMldGroupSrcListHostAddress,
       "me1200IpmcSnoopingMldGroupSrcListGroupFilterMode": me1200IpmcSnoopingMldGroupSrcListGroupFilterMode,
       "me1200IpmcSnoopingMldGroupSrcListFilterTimer": me1200IpmcSnoopingMldGroupSrcListFilterTimer,
       "me1200IpmcSnoopingMldGroupSrcListSourceType": me1200IpmcSnoopingMldGroupSrcListSourceType,
       "me1200IpmcSnoopingMldGroupSrcListSourceTimer": me1200IpmcSnoopingMldGroupSrcListSourceTimer,
       "me1200IpmcSnoopingMldGroupSrcListHardwareFilter": me1200IpmcSnoopingMldGroupSrcListHardwareFilter,
       "me1200IpmcSnoopingControl": me1200IpmcSnoopingControl,
       "me1200IpmcSnoopingControlStatistics": me1200IpmcSnoopingControlStatistics,
       "me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndex": me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndex,
       "me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex": me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexIfIndex,
       "me1200IpmcSnoopingControlStatisticsMldClearByIfIndex": me1200IpmcSnoopingControlStatisticsMldClearByIfIndex,
       "me1200IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex": me1200IpmcSnoopingControlStatisticsMldClearByIfIndexIfIndex,
       "me1200IpmcSnoopingMIBConformance": me1200IpmcSnoopingMIBConformance,
       "me1200IpmcSnoopingMIBCompliances": me1200IpmcSnoopingMIBCompliances,
       "me1200IpmcSnoopingMibCompliance": me1200IpmcSnoopingMibCompliance,
       "me1200IpmcSnoopingMIBGroups": me1200IpmcSnoopingMIBGroups,
       "me1200IpmcSnoopingIgmpGlobalsInfoGroup": me1200IpmcSnoopingIgmpGlobalsInfoGroup,
       "me1200IpmcSnoopingIgmpPortTableInfoGroup": me1200IpmcSnoopingIgmpPortTableInfoGroup,
       "me1200IpmcSnoopingIgmpInterfaceTableInfoGroup": me1200IpmcSnoopingIgmpInterfaceTableInfoGroup,
       "me1200IpmcSnoopingIgmpInterfaceTableRowEditorInfoGroup": me1200IpmcSnoopingIgmpInterfaceTableRowEditorInfoGroup,
       "me1200IpmcSnoopingMldGlobalsInfoGroup": me1200IpmcSnoopingMldGlobalsInfoGroup,
       "me1200IpmcSnoopingMldPortTableInfoGroup": me1200IpmcSnoopingMldPortTableInfoGroup,
       "me1200IpmcSnoopingMldInterfaceTableInfoGroup": me1200IpmcSnoopingMldInterfaceTableInfoGroup,
       "me1200IpmcSnoopingMldInterfaceTableRowEditorInfoGroup": me1200IpmcSnoopingMldInterfaceTableRowEditorInfoGroup,
       "me1200IpmcSnoopingGroupAddressCountInfoGroup": me1200IpmcSnoopingGroupAddressCountInfoGroup,
       "me1200IpmcSnoopingIgmpRouterPortTableInfoGroup": me1200IpmcSnoopingIgmpRouterPortTableInfoGroup,
       "me1200IpmcSnoopingIgmpVlanStatusTableInfoGroup": me1200IpmcSnoopingIgmpVlanStatusTableInfoGroup,
       "me1200IpmcSnoopingIgmpGroupAddressTableInfoGroup": me1200IpmcSnoopingIgmpGroupAddressTableInfoGroup,
       "me1200IpmcSnoopingIgmpGroupSrcListTableInfoGroup": me1200IpmcSnoopingIgmpGroupSrcListTableInfoGroup,
       "me1200IpmcSnoopingMldRouterPortTableInfoGroup": me1200IpmcSnoopingMldRouterPortTableInfoGroup,
       "me1200IpmcSnoopingMldVlanStatusTableInfoGroup": me1200IpmcSnoopingMldVlanStatusTableInfoGroup,
       "me1200IpmcSnoopingMldGroupAddressTableInfoGroup": me1200IpmcSnoopingMldGroupAddressTableInfoGroup,
       "me1200IpmcSnoopingMldGroupSrcListTableInfoGroup": me1200IpmcSnoopingMldGroupSrcListTableInfoGroup,
       "me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup": me1200IpmcSnoopingControlStatisticsIgmpClearByIfIndexInfoGroup,
       "me1200IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup": me1200IpmcSnoopingControlStatisticsMldClearByIfIndexInfoGroup}
)
