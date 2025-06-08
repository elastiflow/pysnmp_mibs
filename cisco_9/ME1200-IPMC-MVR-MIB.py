# SNMP MIB module (ME1200-IPMC-MVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-IPMC-MVR-MIB.mib
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

me1200IpmcMvrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68)
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMib.setRevisions(
        ("2014-03-11 00:00",
         "2014-02-15 00:00",
         "2014-02-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200IpmcMvrVlanInterfaceMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("compatible", 1))
    )



class ME1200IpmcMvrVlanInterfaceTagging(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("untagged", 0),
          ("tagging", 1))
    )



class ME1200IpmcMvrVlanInterfacePortRole(TextualConvention, Integer32):
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
        *(("inactive", 0),
          ("source", 1),
          ("receiver", 2))
    )



class ME1200IpmcMvrInterfaceQuerierStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", -1),
          ("initial", 0),
          ("idle", 1),
          ("active", 2))
    )



class ME1200IpmcMvrGroupSrcListGroupFilterMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 0),
          ("include", 1))
    )



class ME1200IpmcMvrGroupSrcListSourceType(TextualConvention, Integer32):
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

_Me1200IpmcMvrMIBObjects_ObjectIdentity = ObjectIdentity
me1200IpmcMvrMIBObjects = _Me1200IpmcMvrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1)
)
_Me1200IpmcMvrConfig_ObjectIdentity = ObjectIdentity
me1200IpmcMvrConfig = _Me1200IpmcMvrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2)
)
_Me1200IpmcMvrGlobals_ObjectIdentity = ObjectIdentity
me1200IpmcMvrGlobals = _Me1200IpmcMvrGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 1)
)
_Me1200IpmcMvrGlobalsAdminState_Type = TruthValue
_Me1200IpmcMvrGlobalsAdminState_Object = MibScalar
me1200IpmcMvrGlobalsAdminState = _Me1200IpmcMvrGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 1, 1),
    _Me1200IpmcMvrGlobalsAdminState_Type()
)
me1200IpmcMvrGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrGlobalsAdminState.setStatus("current")
_Me1200IpmcMvrPortTable_Object = MibTable
me1200IpmcMvrPortTable = _Me1200IpmcMvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200IpmcMvrPortTable.setStatus("current")
_Me1200IpmcMvrPortEntry_Object = MibTableRow
me1200IpmcMvrPortEntry = _Me1200IpmcMvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 2, 1)
)
me1200IpmcMvrPortEntry.setIndexNames(
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrPortPortIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcMvrPortEntry.setStatus("current")
_Me1200IpmcMvrPortPortIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrPortPortIndex_Object = MibTableColumn
me1200IpmcMvrPortPortIndex = _Me1200IpmcMvrPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 2, 1, 1),
    _Me1200IpmcMvrPortPortIndex_Type()
)
me1200IpmcMvrPortPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrPortPortIndex.setStatus("current")
_Me1200IpmcMvrPortDoImmediateLeave_Type = TruthValue
_Me1200IpmcMvrPortDoImmediateLeave_Object = MibTableColumn
me1200IpmcMvrPortDoImmediateLeave = _Me1200IpmcMvrPortDoImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 2, 1, 2),
    _Me1200IpmcMvrPortDoImmediateLeave_Type()
)
me1200IpmcMvrPortDoImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrPortDoImmediateLeave.setStatus("current")
_Me1200IpmcMvrInterfaceTable_Object = MibTable
me1200IpmcMvrInterfaceTable = _Me1200IpmcMvrInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3)
)
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTable.setStatus("current")
_Me1200IpmcMvrInterfaceEntry_Object = MibTableRow
me1200IpmcMvrInterfaceEntry = _Me1200IpmcMvrInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3, 1)
)
me1200IpmcMvrInterfaceEntry.setIndexNames(
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceEntry.setStatus("current")
_Me1200IpmcMvrInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrInterfaceIfIndex_Object = MibTableColumn
me1200IpmcMvrInterfaceIfIndex = _Me1200IpmcMvrInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3, 1, 1),
    _Me1200IpmcMvrInterfaceIfIndex_Type()
)
me1200IpmcMvrInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceIfIndex.setStatus("current")


class _Me1200IpmcMvrInterfaceName_Type(ME1200DisplayString):
    """Custom type me1200IpmcMvrInterfaceName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcMvrInterfaceName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcMvrInterfaceName_Object = MibTableColumn
me1200IpmcMvrInterfaceName = _Me1200IpmcMvrInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3, 1, 2),
    _Me1200IpmcMvrInterfaceName_Type()
)
me1200IpmcMvrInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceName.setStatus("current")
_Me1200IpmcMvrInterfaceIgmpQuerierAddress_Type = IpAddress
_Me1200IpmcMvrInterfaceIgmpQuerierAddress_Object = MibTableColumn
me1200IpmcMvrInterfaceIgmpQuerierAddress = _Me1200IpmcMvrInterfaceIgmpQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3, 1, 3),
    _Me1200IpmcMvrInterfaceIgmpQuerierAddress_Type()
)
me1200IpmcMvrInterfaceIgmpQuerierAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceIgmpQuerierAddress.setStatus("current")
_Me1200IpmcMvrInterfaceMode_Type = ME1200IpmcMvrVlanInterfaceMode
_Me1200IpmcMvrInterfaceMode_Object = MibTableColumn
me1200IpmcMvrInterfaceMode = _Me1200IpmcMvrInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3, 1, 4),
    _Me1200IpmcMvrInterfaceMode_Type()
)
me1200IpmcMvrInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceMode.setStatus("current")
_Me1200IpmcMvrInterfaceTagging_Type = ME1200IpmcMvrVlanInterfaceTagging
_Me1200IpmcMvrInterfaceTagging_Object = MibTableColumn
me1200IpmcMvrInterfaceTagging = _Me1200IpmcMvrInterfaceTagging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3, 1, 5),
    _Me1200IpmcMvrInterfaceTagging_Type()
)
me1200IpmcMvrInterfaceTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTagging.setStatus("current")
_Me1200IpmcMvrInterfacePriority_Type = ME1200Unsigned8
_Me1200IpmcMvrInterfacePriority_Object = MibTableColumn
me1200IpmcMvrInterfacePriority = _Me1200IpmcMvrInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3, 1, 6),
    _Me1200IpmcMvrInterfacePriority_Type()
)
me1200IpmcMvrInterfacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfacePriority.setStatus("current")
_Me1200IpmcMvrInterfaceLastListenerQueryInterval_Type = Unsigned32
_Me1200IpmcMvrInterfaceLastListenerQueryInterval_Object = MibTableColumn
me1200IpmcMvrInterfaceLastListenerQueryInterval = _Me1200IpmcMvrInterfaceLastListenerQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3, 1, 7),
    _Me1200IpmcMvrInterfaceLastListenerQueryInterval_Type()
)
me1200IpmcMvrInterfaceLastListenerQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceLastListenerQueryInterval.setStatus("current")


class _Me1200IpmcMvrInterfaceChannelProfile_Type(ME1200DisplayString):
    """Custom type me1200IpmcMvrInterfaceChannelProfile based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcMvrInterfaceChannelProfile_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcMvrInterfaceChannelProfile_Object = MibTableColumn
me1200IpmcMvrInterfaceChannelProfile = _Me1200IpmcMvrInterfaceChannelProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3, 1, 8),
    _Me1200IpmcMvrInterfaceChannelProfile_Type()
)
me1200IpmcMvrInterfaceChannelProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceChannelProfile.setStatus("current")
_Me1200IpmcMvrInterfaceAction_Type = ME1200RowEditorState
_Me1200IpmcMvrInterfaceAction_Object = MibTableColumn
me1200IpmcMvrInterfaceAction = _Me1200IpmcMvrInterfaceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 3, 1, 100),
    _Me1200IpmcMvrInterfaceAction_Type()
)
me1200IpmcMvrInterfaceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceAction.setStatus("current")
_Me1200IpmcMvrInterfaceTableRowEditor_ObjectIdentity = ObjectIdentity
me1200IpmcMvrInterfaceTableRowEditor = _Me1200IpmcMvrInterfaceTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 4)
)
_Me1200IpmcMvrInterfaceTableRowEditorIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrInterfaceTableRowEditorIfIndex_Object = MibScalar
me1200IpmcMvrInterfaceTableRowEditorIfIndex = _Me1200IpmcMvrInterfaceTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 4, 1),
    _Me1200IpmcMvrInterfaceTableRowEditorIfIndex_Type()
)
me1200IpmcMvrInterfaceTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableRowEditorIfIndex.setStatus("current")


class _Me1200IpmcMvrInterfaceTableRowEditorName_Type(ME1200DisplayString):
    """Custom type me1200IpmcMvrInterfaceTableRowEditorName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcMvrInterfaceTableRowEditorName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcMvrInterfaceTableRowEditorName_Object = MibScalar
me1200IpmcMvrInterfaceTableRowEditorName = _Me1200IpmcMvrInterfaceTableRowEditorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 4, 2),
    _Me1200IpmcMvrInterfaceTableRowEditorName_Type()
)
me1200IpmcMvrInterfaceTableRowEditorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableRowEditorName.setStatus("current")
_Me1200IpmcMvrInterfaceTableRowEditorIgmpQuerierAddress_Type = IpAddress
_Me1200IpmcMvrInterfaceTableRowEditorIgmpQuerierAddress_Object = MibScalar
me1200IpmcMvrInterfaceTableRowEditorIgmpQuerierAddress = _Me1200IpmcMvrInterfaceTableRowEditorIgmpQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 4, 3),
    _Me1200IpmcMvrInterfaceTableRowEditorIgmpQuerierAddress_Type()
)
me1200IpmcMvrInterfaceTableRowEditorIgmpQuerierAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableRowEditorIgmpQuerierAddress.setStatus("current")
_Me1200IpmcMvrInterfaceTableRowEditorMode_Type = ME1200IpmcMvrVlanInterfaceMode
_Me1200IpmcMvrInterfaceTableRowEditorMode_Object = MibScalar
me1200IpmcMvrInterfaceTableRowEditorMode = _Me1200IpmcMvrInterfaceTableRowEditorMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 4, 4),
    _Me1200IpmcMvrInterfaceTableRowEditorMode_Type()
)
me1200IpmcMvrInterfaceTableRowEditorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableRowEditorMode.setStatus("current")
_Me1200IpmcMvrInterfaceTableRowEditorTagging_Type = ME1200IpmcMvrVlanInterfaceTagging
_Me1200IpmcMvrInterfaceTableRowEditorTagging_Object = MibScalar
me1200IpmcMvrInterfaceTableRowEditorTagging = _Me1200IpmcMvrInterfaceTableRowEditorTagging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 4, 5),
    _Me1200IpmcMvrInterfaceTableRowEditorTagging_Type()
)
me1200IpmcMvrInterfaceTableRowEditorTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableRowEditorTagging.setStatus("current")
_Me1200IpmcMvrInterfaceTableRowEditorPriority_Type = ME1200Unsigned8
_Me1200IpmcMvrInterfaceTableRowEditorPriority_Object = MibScalar
me1200IpmcMvrInterfaceTableRowEditorPriority = _Me1200IpmcMvrInterfaceTableRowEditorPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 4, 6),
    _Me1200IpmcMvrInterfaceTableRowEditorPriority_Type()
)
me1200IpmcMvrInterfaceTableRowEditorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableRowEditorPriority.setStatus("current")
_Me1200IpmcMvrInterfaceTableRowEditorLastListenerQueryInterval_Type = Unsigned32
_Me1200IpmcMvrInterfaceTableRowEditorLastListenerQueryInterval_Object = MibScalar
me1200IpmcMvrInterfaceTableRowEditorLastListenerQueryInterval = _Me1200IpmcMvrInterfaceTableRowEditorLastListenerQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 4, 7),
    _Me1200IpmcMvrInterfaceTableRowEditorLastListenerQueryInterval_Type()
)
me1200IpmcMvrInterfaceTableRowEditorLastListenerQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableRowEditorLastListenerQueryInterval.setStatus("current")


class _Me1200IpmcMvrInterfaceTableRowEditorChannelProfile_Type(ME1200DisplayString):
    """Custom type me1200IpmcMvrInterfaceTableRowEditorChannelProfile based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcMvrInterfaceTableRowEditorChannelProfile_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcMvrInterfaceTableRowEditorChannelProfile_Object = MibScalar
me1200IpmcMvrInterfaceTableRowEditorChannelProfile = _Me1200IpmcMvrInterfaceTableRowEditorChannelProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 4, 8),
    _Me1200IpmcMvrInterfaceTableRowEditorChannelProfile_Type()
)
me1200IpmcMvrInterfaceTableRowEditorChannelProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableRowEditorChannelProfile.setStatus("current")
_Me1200IpmcMvrInterfaceTableRowEditorAction_Type = ME1200RowEditorState
_Me1200IpmcMvrInterfaceTableRowEditorAction_Object = MibScalar
me1200IpmcMvrInterfaceTableRowEditorAction = _Me1200IpmcMvrInterfaceTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 4, 100),
    _Me1200IpmcMvrInterfaceTableRowEditorAction_Type()
)
me1200IpmcMvrInterfaceTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableRowEditorAction.setStatus("current")
_Me1200IpmcMvrVlanPortTable_Object = MibTable
me1200IpmcMvrVlanPortTable = _Me1200IpmcMvrVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 5)
)
if mibBuilder.loadTexts:
    me1200IpmcMvrVlanPortTable.setStatus("current")
_Me1200IpmcMvrVlanPortEntry_Object = MibTableRow
me1200IpmcMvrVlanPortEntry = _Me1200IpmcMvrVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 5, 1)
)
me1200IpmcMvrVlanPortEntry.setIndexNames(
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrVlanPortIfIndex"),
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrVlanPortPortIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcMvrVlanPortEntry.setStatus("current")
_Me1200IpmcMvrVlanPortIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrVlanPortIfIndex_Object = MibTableColumn
me1200IpmcMvrVlanPortIfIndex = _Me1200IpmcMvrVlanPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 5, 1, 1),
    _Me1200IpmcMvrVlanPortIfIndex_Type()
)
me1200IpmcMvrVlanPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrVlanPortIfIndex.setStatus("current")
_Me1200IpmcMvrVlanPortPortIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrVlanPortPortIndex_Object = MibTableColumn
me1200IpmcMvrVlanPortPortIndex = _Me1200IpmcMvrVlanPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 5, 1, 2),
    _Me1200IpmcMvrVlanPortPortIndex_Type()
)
me1200IpmcMvrVlanPortPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrVlanPortPortIndex.setStatus("current")
_Me1200IpmcMvrVlanPortRole_Type = ME1200IpmcMvrVlanInterfacePortRole
_Me1200IpmcMvrVlanPortRole_Object = MibTableColumn
me1200IpmcMvrVlanPortRole = _Me1200IpmcMvrVlanPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 2, 5, 1, 3),
    _Me1200IpmcMvrVlanPortRole_Type()
)
me1200IpmcMvrVlanPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrVlanPortRole.setStatus("current")
_Me1200IpmcMvrStatus_ObjectIdentity = ObjectIdentity
me1200IpmcMvrStatus = _Me1200IpmcMvrStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3)
)
_Me1200IpmcMvrGroupAddressCount_ObjectIdentity = ObjectIdentity
me1200IpmcMvrGroupAddressCount = _Me1200IpmcMvrGroupAddressCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 1)
)
_Me1200IpmcMvrGroupAddressCountFromIgmp_Type = Unsigned32
_Me1200IpmcMvrGroupAddressCountFromIgmp_Object = MibScalar
me1200IpmcMvrGroupAddressCountFromIgmp = _Me1200IpmcMvrGroupAddressCountFromIgmp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 1, 1),
    _Me1200IpmcMvrGroupAddressCountFromIgmp_Type()
)
me1200IpmcMvrGroupAddressCountFromIgmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrGroupAddressCountFromIgmp.setStatus("current")
_Me1200IpmcMvrGroupAddressCountFromMld_Type = Unsigned32
_Me1200IpmcMvrGroupAddressCountFromMld_Object = MibScalar
me1200IpmcMvrGroupAddressCountFromMld = _Me1200IpmcMvrGroupAddressCountFromMld_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 1, 2),
    _Me1200IpmcMvrGroupAddressCountFromMld_Type()
)
me1200IpmcMvrGroupAddressCountFromMld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrGroupAddressCountFromMld.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusTable_Object = MibTable
me1200IpmcMvrIgmpVlanStatusTable = _Me1200IpmcMvrIgmpVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusTable.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusEntry_Object = MibTableRow
me1200IpmcMvrIgmpVlanStatusEntry = _Me1200IpmcMvrIgmpVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1)
)
me1200IpmcMvrIgmpVlanStatusEntry.setIndexNames(
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusEntry.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrIgmpVlanStatusIfIndex_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusIfIndex = _Me1200IpmcMvrIgmpVlanStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 1),
    _Me1200IpmcMvrIgmpVlanStatusIfIndex_Type()
)
me1200IpmcMvrIgmpVlanStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusIfIndex.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusQuerierStatus_Type = ME1200IpmcMvrInterfaceQuerierStatus
_Me1200IpmcMvrIgmpVlanStatusQuerierStatus_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusQuerierStatus = _Me1200IpmcMvrIgmpVlanStatusQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 2),
    _Me1200IpmcMvrIgmpVlanStatusQuerierStatus_Type()
)
me1200IpmcMvrIgmpVlanStatusQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusQuerierStatus.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusActiveQuerierAddress_Type = IpAddress
_Me1200IpmcMvrIgmpVlanStatusActiveQuerierAddress_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusActiveQuerierAddress = _Me1200IpmcMvrIgmpVlanStatusActiveQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 3),
    _Me1200IpmcMvrIgmpVlanStatusActiveQuerierAddress_Type()
)
me1200IpmcMvrIgmpVlanStatusActiveQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusActiveQuerierAddress.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusQuerierUptime_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusQuerierUptime_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusQuerierUptime = _Me1200IpmcMvrIgmpVlanStatusQuerierUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 4),
    _Me1200IpmcMvrIgmpVlanStatusQuerierUptime_Type()
)
me1200IpmcMvrIgmpVlanStatusQuerierUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusQuerierUptime.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusQueryInterval_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusQueryInterval_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusQueryInterval = _Me1200IpmcMvrIgmpVlanStatusQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 5),
    _Me1200IpmcMvrIgmpVlanStatusQueryInterval_Type()
)
me1200IpmcMvrIgmpVlanStatusQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusQueryInterval.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusStartupQueryCount_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusStartupQueryCount_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusStartupQueryCount = _Me1200IpmcMvrIgmpVlanStatusStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 6),
    _Me1200IpmcMvrIgmpVlanStatusStartupQueryCount_Type()
)
me1200IpmcMvrIgmpVlanStatusStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusStartupQueryCount.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusQuerierExpiryTime_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusQuerierExpiryTime_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusQuerierExpiryTime = _Me1200IpmcMvrIgmpVlanStatusQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 7),
    _Me1200IpmcMvrIgmpVlanStatusQuerierExpiryTime_Type()
)
me1200IpmcMvrIgmpVlanStatusQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusQuerierExpiryTime.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusCounterTxQuery_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusCounterTxQuery_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusCounterTxQuery = _Me1200IpmcMvrIgmpVlanStatusCounterTxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 8),
    _Me1200IpmcMvrIgmpVlanStatusCounterTxQuery_Type()
)
me1200IpmcMvrIgmpVlanStatusCounterTxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusCounterTxQuery.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusCounterTxSpecificQuery_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusCounterTxSpecificQuery_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusCounterTxSpecificQuery = _Me1200IpmcMvrIgmpVlanStatusCounterTxSpecificQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 9),
    _Me1200IpmcMvrIgmpVlanStatusCounterTxSpecificQuery_Type()
)
me1200IpmcMvrIgmpVlanStatusCounterTxSpecificQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusCounterTxSpecificQuery.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusCounterRxQuery_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusCounterRxQuery_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusCounterRxQuery = _Me1200IpmcMvrIgmpVlanStatusCounterRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 10),
    _Me1200IpmcMvrIgmpVlanStatusCounterRxQuery_Type()
)
me1200IpmcMvrIgmpVlanStatusCounterRxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusCounterRxQuery.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusCounterRxV1Join_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusCounterRxV1Join_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusCounterRxV1Join = _Me1200IpmcMvrIgmpVlanStatusCounterRxV1Join_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 11),
    _Me1200IpmcMvrIgmpVlanStatusCounterRxV1Join_Type()
)
me1200IpmcMvrIgmpVlanStatusCounterRxV1Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusCounterRxV1Join.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusCounterRxV2Join_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusCounterRxV2Join_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusCounterRxV2Join = _Me1200IpmcMvrIgmpVlanStatusCounterRxV2Join_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 12),
    _Me1200IpmcMvrIgmpVlanStatusCounterRxV2Join_Type()
)
me1200IpmcMvrIgmpVlanStatusCounterRxV2Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusCounterRxV2Join.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusCounterRxV2Leave_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusCounterRxV2Leave_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusCounterRxV2Leave = _Me1200IpmcMvrIgmpVlanStatusCounterRxV2Leave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 13),
    _Me1200IpmcMvrIgmpVlanStatusCounterRxV2Leave_Type()
)
me1200IpmcMvrIgmpVlanStatusCounterRxV2Leave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusCounterRxV2Leave.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusCounterRxV3Join_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusCounterRxV3Join_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusCounterRxV3Join = _Me1200IpmcMvrIgmpVlanStatusCounterRxV3Join_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 14),
    _Me1200IpmcMvrIgmpVlanStatusCounterRxV3Join_Type()
)
me1200IpmcMvrIgmpVlanStatusCounterRxV3Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusCounterRxV3Join.setStatus("current")
_Me1200IpmcMvrIgmpVlanStatusCounterRxErrors_Type = Unsigned32
_Me1200IpmcMvrIgmpVlanStatusCounterRxErrors_Object = MibTableColumn
me1200IpmcMvrIgmpVlanStatusCounterRxErrors = _Me1200IpmcMvrIgmpVlanStatusCounterRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 2, 1, 15),
    _Me1200IpmcMvrIgmpVlanStatusCounterRxErrors_Type()
)
me1200IpmcMvrIgmpVlanStatusCounterRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusCounterRxErrors.setStatus("current")
_Me1200IpmcMvrIgmpGroupAddressTable_Object = MibTable
me1200IpmcMvrIgmpGroupAddressTable = _Me1200IpmcMvrIgmpGroupAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupAddressTable.setStatus("current")
_Me1200IpmcMvrIgmpGroupAddressEntry_Object = MibTableRow
me1200IpmcMvrIgmpGroupAddressEntry = _Me1200IpmcMvrIgmpGroupAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 3, 1)
)
me1200IpmcMvrIgmpGroupAddressEntry.setIndexNames(
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupAddressIfIndex"),
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupAddressGroupAddress"),
)
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupAddressEntry.setStatus("current")
_Me1200IpmcMvrIgmpGroupAddressIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrIgmpGroupAddressIfIndex_Object = MibTableColumn
me1200IpmcMvrIgmpGroupAddressIfIndex = _Me1200IpmcMvrIgmpGroupAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 3, 1, 1),
    _Me1200IpmcMvrIgmpGroupAddressIfIndex_Type()
)
me1200IpmcMvrIgmpGroupAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupAddressIfIndex.setStatus("current")
_Me1200IpmcMvrIgmpGroupAddressGroupAddress_Type = IpAddress
_Me1200IpmcMvrIgmpGroupAddressGroupAddress_Object = MibTableColumn
me1200IpmcMvrIgmpGroupAddressGroupAddress = _Me1200IpmcMvrIgmpGroupAddressGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 3, 1, 2),
    _Me1200IpmcMvrIgmpGroupAddressGroupAddress_Type()
)
me1200IpmcMvrIgmpGroupAddressGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupAddressGroupAddress.setStatus("current")
_Me1200IpmcMvrIgmpGroupAddressMemberPorts_Type = ME1200PortListStackable
_Me1200IpmcMvrIgmpGroupAddressMemberPorts_Object = MibTableColumn
me1200IpmcMvrIgmpGroupAddressMemberPorts = _Me1200IpmcMvrIgmpGroupAddressMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 3, 1, 3),
    _Me1200IpmcMvrIgmpGroupAddressMemberPorts_Type()
)
me1200IpmcMvrIgmpGroupAddressMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupAddressMemberPorts.setStatus("current")
_Me1200IpmcMvrIgmpGroupAddressHardwareSwitch_Type = TruthValue
_Me1200IpmcMvrIgmpGroupAddressHardwareSwitch_Object = MibTableColumn
me1200IpmcMvrIgmpGroupAddressHardwareSwitch = _Me1200IpmcMvrIgmpGroupAddressHardwareSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 3, 1, 4),
    _Me1200IpmcMvrIgmpGroupAddressHardwareSwitch_Type()
)
me1200IpmcMvrIgmpGroupAddressHardwareSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupAddressHardwareSwitch.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListTable_Object = MibTable
me1200IpmcMvrIgmpGroupSrcListTable = _Me1200IpmcMvrIgmpGroupSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4)
)
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListTable.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListEntry_Object = MibTableRow
me1200IpmcMvrIgmpGroupSrcListEntry = _Me1200IpmcMvrIgmpGroupSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4, 1)
)
me1200IpmcMvrIgmpGroupSrcListEntry.setIndexNames(
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupSrcListIfIndex"),
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupSrcListGroupAddress"),
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupSrcListPortIndex"),
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListEntry.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrIgmpGroupSrcListIfIndex_Object = MibTableColumn
me1200IpmcMvrIgmpGroupSrcListIfIndex = _Me1200IpmcMvrIgmpGroupSrcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4, 1, 1),
    _Me1200IpmcMvrIgmpGroupSrcListIfIndex_Type()
)
me1200IpmcMvrIgmpGroupSrcListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListIfIndex.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListGroupAddress_Type = IpAddress
_Me1200IpmcMvrIgmpGroupSrcListGroupAddress_Object = MibTableColumn
me1200IpmcMvrIgmpGroupSrcListGroupAddress = _Me1200IpmcMvrIgmpGroupSrcListGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4, 1, 2),
    _Me1200IpmcMvrIgmpGroupSrcListGroupAddress_Type()
)
me1200IpmcMvrIgmpGroupSrcListGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListGroupAddress.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListPortIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrIgmpGroupSrcListPortIndex_Object = MibTableColumn
me1200IpmcMvrIgmpGroupSrcListPortIndex = _Me1200IpmcMvrIgmpGroupSrcListPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4, 1, 3),
    _Me1200IpmcMvrIgmpGroupSrcListPortIndex_Type()
)
me1200IpmcMvrIgmpGroupSrcListPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListPortIndex.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListHostAddress_Type = IpAddress
_Me1200IpmcMvrIgmpGroupSrcListHostAddress_Object = MibTableColumn
me1200IpmcMvrIgmpGroupSrcListHostAddress = _Me1200IpmcMvrIgmpGroupSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4, 1, 4),
    _Me1200IpmcMvrIgmpGroupSrcListHostAddress_Type()
)
me1200IpmcMvrIgmpGroupSrcListHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListHostAddress.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListGroupFilterMode_Type = ME1200IpmcMvrGroupSrcListGroupFilterMode
_Me1200IpmcMvrIgmpGroupSrcListGroupFilterMode_Object = MibTableColumn
me1200IpmcMvrIgmpGroupSrcListGroupFilterMode = _Me1200IpmcMvrIgmpGroupSrcListGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4, 1, 5),
    _Me1200IpmcMvrIgmpGroupSrcListGroupFilterMode_Type()
)
me1200IpmcMvrIgmpGroupSrcListGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListGroupFilterMode.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListFilterTimer_Type = Unsigned32
_Me1200IpmcMvrIgmpGroupSrcListFilterTimer_Object = MibTableColumn
me1200IpmcMvrIgmpGroupSrcListFilterTimer = _Me1200IpmcMvrIgmpGroupSrcListFilterTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4, 1, 6),
    _Me1200IpmcMvrIgmpGroupSrcListFilterTimer_Type()
)
me1200IpmcMvrIgmpGroupSrcListFilterTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListFilterTimer.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListSourceType_Type = ME1200IpmcMvrGroupSrcListSourceType
_Me1200IpmcMvrIgmpGroupSrcListSourceType_Object = MibTableColumn
me1200IpmcMvrIgmpGroupSrcListSourceType = _Me1200IpmcMvrIgmpGroupSrcListSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4, 1, 7),
    _Me1200IpmcMvrIgmpGroupSrcListSourceType_Type()
)
me1200IpmcMvrIgmpGroupSrcListSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListSourceType.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListSourceTimer_Type = Unsigned32
_Me1200IpmcMvrIgmpGroupSrcListSourceTimer_Object = MibTableColumn
me1200IpmcMvrIgmpGroupSrcListSourceTimer = _Me1200IpmcMvrIgmpGroupSrcListSourceTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4, 1, 8),
    _Me1200IpmcMvrIgmpGroupSrcListSourceTimer_Type()
)
me1200IpmcMvrIgmpGroupSrcListSourceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListSourceTimer.setStatus("current")
_Me1200IpmcMvrIgmpGroupSrcListHardwareFilter_Type = TruthValue
_Me1200IpmcMvrIgmpGroupSrcListHardwareFilter_Object = MibTableColumn
me1200IpmcMvrIgmpGroupSrcListHardwareFilter = _Me1200IpmcMvrIgmpGroupSrcListHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 4, 1, 9),
    _Me1200IpmcMvrIgmpGroupSrcListHardwareFilter_Type()
)
me1200IpmcMvrIgmpGroupSrcListHardwareFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListHardwareFilter.setStatus("current")
_Me1200IpmcMvrMldVlanStatusTable_Object = MibTable
me1200IpmcMvrMldVlanStatusTable = _Me1200IpmcMvrMldVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5)
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusTable.setStatus("current")
_Me1200IpmcMvrMldVlanStatusEntry_Object = MibTableRow
me1200IpmcMvrMldVlanStatusEntry = _Me1200IpmcMvrMldVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1)
)
me1200IpmcMvrMldVlanStatusEntry.setIndexNames(
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusEntry.setStatus("current")
_Me1200IpmcMvrMldVlanStatusIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrMldVlanStatusIfIndex_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusIfIndex = _Me1200IpmcMvrMldVlanStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 1),
    _Me1200IpmcMvrMldVlanStatusIfIndex_Type()
)
me1200IpmcMvrMldVlanStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusIfIndex.setStatus("current")
_Me1200IpmcMvrMldVlanStatusQuerierStatus_Type = ME1200IpmcMvrInterfaceQuerierStatus
_Me1200IpmcMvrMldVlanStatusQuerierStatus_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusQuerierStatus = _Me1200IpmcMvrMldVlanStatusQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 2),
    _Me1200IpmcMvrMldVlanStatusQuerierStatus_Type()
)
me1200IpmcMvrMldVlanStatusQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusQuerierStatus.setStatus("current")
_Me1200IpmcMvrMldVlanStatusActiveQuerierAddress_Type = InetAddressIPv6
_Me1200IpmcMvrMldVlanStatusActiveQuerierAddress_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusActiveQuerierAddress = _Me1200IpmcMvrMldVlanStatusActiveQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 3),
    _Me1200IpmcMvrMldVlanStatusActiveQuerierAddress_Type()
)
me1200IpmcMvrMldVlanStatusActiveQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusActiveQuerierAddress.setStatus("current")
_Me1200IpmcMvrMldVlanStatusQuerierUptime_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusQuerierUptime_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusQuerierUptime = _Me1200IpmcMvrMldVlanStatusQuerierUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 4),
    _Me1200IpmcMvrMldVlanStatusQuerierUptime_Type()
)
me1200IpmcMvrMldVlanStatusQuerierUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusQuerierUptime.setStatus("current")
_Me1200IpmcMvrMldVlanStatusQueryInterval_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusQueryInterval_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusQueryInterval = _Me1200IpmcMvrMldVlanStatusQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 5),
    _Me1200IpmcMvrMldVlanStatusQueryInterval_Type()
)
me1200IpmcMvrMldVlanStatusQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusQueryInterval.setStatus("current")
_Me1200IpmcMvrMldVlanStatusStartupQueryCount_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusStartupQueryCount_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusStartupQueryCount = _Me1200IpmcMvrMldVlanStatusStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 6),
    _Me1200IpmcMvrMldVlanStatusStartupQueryCount_Type()
)
me1200IpmcMvrMldVlanStatusStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusStartupQueryCount.setStatus("current")
_Me1200IpmcMvrMldVlanStatusQuerierExpiryTime_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusQuerierExpiryTime_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusQuerierExpiryTime = _Me1200IpmcMvrMldVlanStatusQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 7),
    _Me1200IpmcMvrMldVlanStatusQuerierExpiryTime_Type()
)
me1200IpmcMvrMldVlanStatusQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusQuerierExpiryTime.setStatus("current")
_Me1200IpmcMvrMldVlanStatusCounterTxQuery_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusCounterTxQuery_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusCounterTxQuery = _Me1200IpmcMvrMldVlanStatusCounterTxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 8),
    _Me1200IpmcMvrMldVlanStatusCounterTxQuery_Type()
)
me1200IpmcMvrMldVlanStatusCounterTxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusCounterTxQuery.setStatus("current")
_Me1200IpmcMvrMldVlanStatusCounterTxSpecificQuery_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusCounterTxSpecificQuery_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusCounterTxSpecificQuery = _Me1200IpmcMvrMldVlanStatusCounterTxSpecificQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 9),
    _Me1200IpmcMvrMldVlanStatusCounterTxSpecificQuery_Type()
)
me1200IpmcMvrMldVlanStatusCounterTxSpecificQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusCounterTxSpecificQuery.setStatus("current")
_Me1200IpmcMvrMldVlanStatusCounterRxQuery_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusCounterRxQuery_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusCounterRxQuery = _Me1200IpmcMvrMldVlanStatusCounterRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 10),
    _Me1200IpmcMvrMldVlanStatusCounterRxQuery_Type()
)
me1200IpmcMvrMldVlanStatusCounterRxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusCounterRxQuery.setStatus("current")
_Me1200IpmcMvrMldVlanStatusCounterRxV1Report_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusCounterRxV1Report_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusCounterRxV1Report = _Me1200IpmcMvrMldVlanStatusCounterRxV1Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 11),
    _Me1200IpmcMvrMldVlanStatusCounterRxV1Report_Type()
)
me1200IpmcMvrMldVlanStatusCounterRxV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusCounterRxV1Report.setStatus("current")
_Me1200IpmcMvrMldVlanStatusCounterRxV1Done_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusCounterRxV1Done_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusCounterRxV1Done = _Me1200IpmcMvrMldVlanStatusCounterRxV1Done_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 12),
    _Me1200IpmcMvrMldVlanStatusCounterRxV1Done_Type()
)
me1200IpmcMvrMldVlanStatusCounterRxV1Done.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusCounterRxV1Done.setStatus("current")
_Me1200IpmcMvrMldVlanStatusCounterRxV2Report_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusCounterRxV2Report_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusCounterRxV2Report = _Me1200IpmcMvrMldVlanStatusCounterRxV2Report_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 13),
    _Me1200IpmcMvrMldVlanStatusCounterRxV2Report_Type()
)
me1200IpmcMvrMldVlanStatusCounterRxV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusCounterRxV2Report.setStatus("current")
_Me1200IpmcMvrMldVlanStatusCounterRxErrors_Type = Unsigned32
_Me1200IpmcMvrMldVlanStatusCounterRxErrors_Object = MibTableColumn
me1200IpmcMvrMldVlanStatusCounterRxErrors = _Me1200IpmcMvrMldVlanStatusCounterRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 5, 1, 14),
    _Me1200IpmcMvrMldVlanStatusCounterRxErrors_Type()
)
me1200IpmcMvrMldVlanStatusCounterRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusCounterRxErrors.setStatus("current")
_Me1200IpmcMvrMldGroupAddressTable_Object = MibTable
me1200IpmcMvrMldGroupAddressTable = _Me1200IpmcMvrMldGroupAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 6)
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupAddressTable.setStatus("current")
_Me1200IpmcMvrMldGroupAddressEntry_Object = MibTableRow
me1200IpmcMvrMldGroupAddressEntry = _Me1200IpmcMvrMldGroupAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 6, 1)
)
me1200IpmcMvrMldGroupAddressEntry.setIndexNames(
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupAddressIfIndex"),
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupAddressGroupAddress"),
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupAddressEntry.setStatus("current")
_Me1200IpmcMvrMldGroupAddressIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrMldGroupAddressIfIndex_Object = MibTableColumn
me1200IpmcMvrMldGroupAddressIfIndex = _Me1200IpmcMvrMldGroupAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 6, 1, 1),
    _Me1200IpmcMvrMldGroupAddressIfIndex_Type()
)
me1200IpmcMvrMldGroupAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupAddressIfIndex.setStatus("current")
_Me1200IpmcMvrMldGroupAddressGroupAddress_Type = InetAddressIPv6
_Me1200IpmcMvrMldGroupAddressGroupAddress_Object = MibTableColumn
me1200IpmcMvrMldGroupAddressGroupAddress = _Me1200IpmcMvrMldGroupAddressGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 6, 1, 2),
    _Me1200IpmcMvrMldGroupAddressGroupAddress_Type()
)
me1200IpmcMvrMldGroupAddressGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupAddressGroupAddress.setStatus("current")
_Me1200IpmcMvrMldGroupAddressMemberPorts_Type = ME1200PortListStackable
_Me1200IpmcMvrMldGroupAddressMemberPorts_Object = MibTableColumn
me1200IpmcMvrMldGroupAddressMemberPorts = _Me1200IpmcMvrMldGroupAddressMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 6, 1, 3),
    _Me1200IpmcMvrMldGroupAddressMemberPorts_Type()
)
me1200IpmcMvrMldGroupAddressMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupAddressMemberPorts.setStatus("current")
_Me1200IpmcMvrMldGroupAddressHardwareSwitch_Type = TruthValue
_Me1200IpmcMvrMldGroupAddressHardwareSwitch_Object = MibTableColumn
me1200IpmcMvrMldGroupAddressHardwareSwitch = _Me1200IpmcMvrMldGroupAddressHardwareSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 6, 1, 4),
    _Me1200IpmcMvrMldGroupAddressHardwareSwitch_Type()
)
me1200IpmcMvrMldGroupAddressHardwareSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupAddressHardwareSwitch.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListTable_Object = MibTable
me1200IpmcMvrMldGroupSrcListTable = _Me1200IpmcMvrMldGroupSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7)
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListTable.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListEntry_Object = MibTableRow
me1200IpmcMvrMldGroupSrcListEntry = _Me1200IpmcMvrMldGroupSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7, 1)
)
me1200IpmcMvrMldGroupSrcListEntry.setIndexNames(
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupSrcListIfIndex"),
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupSrcListGroupAddress"),
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupSrcListPortIndex"),
    (0, "ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListEntry.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrMldGroupSrcListIfIndex_Object = MibTableColumn
me1200IpmcMvrMldGroupSrcListIfIndex = _Me1200IpmcMvrMldGroupSrcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7, 1, 1),
    _Me1200IpmcMvrMldGroupSrcListIfIndex_Type()
)
me1200IpmcMvrMldGroupSrcListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListIfIndex.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListGroupAddress_Type = InetAddressIPv6
_Me1200IpmcMvrMldGroupSrcListGroupAddress_Object = MibTableColumn
me1200IpmcMvrMldGroupSrcListGroupAddress = _Me1200IpmcMvrMldGroupSrcListGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7, 1, 2),
    _Me1200IpmcMvrMldGroupSrcListGroupAddress_Type()
)
me1200IpmcMvrMldGroupSrcListGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListGroupAddress.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListPortIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrMldGroupSrcListPortIndex_Object = MibTableColumn
me1200IpmcMvrMldGroupSrcListPortIndex = _Me1200IpmcMvrMldGroupSrcListPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7, 1, 3),
    _Me1200IpmcMvrMldGroupSrcListPortIndex_Type()
)
me1200IpmcMvrMldGroupSrcListPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListPortIndex.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListHostAddress_Type = InetAddressIPv6
_Me1200IpmcMvrMldGroupSrcListHostAddress_Object = MibTableColumn
me1200IpmcMvrMldGroupSrcListHostAddress = _Me1200IpmcMvrMldGroupSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7, 1, 4),
    _Me1200IpmcMvrMldGroupSrcListHostAddress_Type()
)
me1200IpmcMvrMldGroupSrcListHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListHostAddress.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListGroupFilterMode_Type = ME1200IpmcMvrGroupSrcListGroupFilterMode
_Me1200IpmcMvrMldGroupSrcListGroupFilterMode_Object = MibTableColumn
me1200IpmcMvrMldGroupSrcListGroupFilterMode = _Me1200IpmcMvrMldGroupSrcListGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7, 1, 5),
    _Me1200IpmcMvrMldGroupSrcListGroupFilterMode_Type()
)
me1200IpmcMvrMldGroupSrcListGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListGroupFilterMode.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListFilterTimer_Type = Unsigned32
_Me1200IpmcMvrMldGroupSrcListFilterTimer_Object = MibTableColumn
me1200IpmcMvrMldGroupSrcListFilterTimer = _Me1200IpmcMvrMldGroupSrcListFilterTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7, 1, 6),
    _Me1200IpmcMvrMldGroupSrcListFilterTimer_Type()
)
me1200IpmcMvrMldGroupSrcListFilterTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListFilterTimer.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListSourceType_Type = ME1200IpmcMvrGroupSrcListSourceType
_Me1200IpmcMvrMldGroupSrcListSourceType_Object = MibTableColumn
me1200IpmcMvrMldGroupSrcListSourceType = _Me1200IpmcMvrMldGroupSrcListSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7, 1, 7),
    _Me1200IpmcMvrMldGroupSrcListSourceType_Type()
)
me1200IpmcMvrMldGroupSrcListSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListSourceType.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListSourceTimer_Type = Unsigned32
_Me1200IpmcMvrMldGroupSrcListSourceTimer_Object = MibTableColumn
me1200IpmcMvrMldGroupSrcListSourceTimer = _Me1200IpmcMvrMldGroupSrcListSourceTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7, 1, 8),
    _Me1200IpmcMvrMldGroupSrcListSourceTimer_Type()
)
me1200IpmcMvrMldGroupSrcListSourceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListSourceTimer.setStatus("current")
_Me1200IpmcMvrMldGroupSrcListHardwareFilter_Type = TruthValue
_Me1200IpmcMvrMldGroupSrcListHardwareFilter_Object = MibTableColumn
me1200IpmcMvrMldGroupSrcListHardwareFilter = _Me1200IpmcMvrMldGroupSrcListHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 3, 7, 1, 9),
    _Me1200IpmcMvrMldGroupSrcListHardwareFilter_Type()
)
me1200IpmcMvrMldGroupSrcListHardwareFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListHardwareFilter.setStatus("current")
_Me1200IpmcMvrControl_ObjectIdentity = ObjectIdentity
me1200IpmcMvrControl = _Me1200IpmcMvrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 4)
)
_Me1200IpmcMvrControlStatisticsClear_ObjectIdentity = ObjectIdentity
me1200IpmcMvrControlStatisticsClear = _Me1200IpmcMvrControlStatisticsClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 4, 1)
)
_Me1200IpmcMvrControlStatisticsClearIfIndex_Type = ME1200InterfaceIndex
_Me1200IpmcMvrControlStatisticsClearIfIndex_Object = MibScalar
me1200IpmcMvrControlStatisticsClearIfIndex = _Me1200IpmcMvrControlStatisticsClearIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 1, 4, 1, 1),
    _Me1200IpmcMvrControlStatisticsClearIfIndex_Type()
)
me1200IpmcMvrControlStatisticsClearIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcMvrControlStatisticsClearIfIndex.setStatus("current")
_Me1200IpmcMvrMIBConformance_ObjectIdentity = ObjectIdentity
me1200IpmcMvrMIBConformance = _Me1200IpmcMvrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2)
)
_Me1200IpmcMvrMIBCompliances_ObjectIdentity = ObjectIdentity
me1200IpmcMvrMIBCompliances = _Me1200IpmcMvrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 1)
)
_Me1200IpmcMvrMIBGroups_ObjectIdentity = ObjectIdentity
me1200IpmcMvrMIBGroups = _Me1200IpmcMvrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2)
)

# Managed Objects groups

me1200IpmcMvrGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 1)
)
me1200IpmcMvrGlobalsInfoGroup.setObjects(
    ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrGlobalsAdminState")
)
if mibBuilder.loadTexts:
    me1200IpmcMvrGlobalsInfoGroup.setStatus("current")

me1200IpmcMvrPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 2)
)
me1200IpmcMvrPortTableInfoGroup.setObjects(
    ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrPortDoImmediateLeave")
)
if mibBuilder.loadTexts:
    me1200IpmcMvrPortTableInfoGroup.setStatus("current")

me1200IpmcMvrInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 3)
)
me1200IpmcMvrInterfaceTableInfoGroup.setObjects(
      *(("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceName"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceIgmpQuerierAddress"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceMode"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTagging"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfacePriority"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceLastListenerQueryInterval"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceChannelProfile"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableInfoGroup.setStatus("current")

me1200IpmcMvrInterfaceTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 4)
)
me1200IpmcMvrInterfaceTableRowEditorInfoGroup.setObjects(
      *(("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableRowEditorIfIndex"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableRowEditorName"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableRowEditorIgmpQuerierAddress"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableRowEditorMode"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableRowEditorTagging"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableRowEditorPriority"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableRowEditorLastListenerQueryInterval"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableRowEditorChannelProfile"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcMvrInterfaceTableRowEditorInfoGroup.setStatus("current")

me1200IpmcMvrVlanPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 5)
)
me1200IpmcMvrVlanPortTableInfoGroup.setObjects(
    ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrVlanPortRole")
)
if mibBuilder.loadTexts:
    me1200IpmcMvrVlanPortTableInfoGroup.setStatus("current")

me1200IpmcMvrGroupAddressCountInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 6)
)
me1200IpmcMvrGroupAddressCountInfoGroup.setObjects(
      *(("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrGroupAddressCountFromIgmp"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrGroupAddressCountFromMld"))
)
if mibBuilder.loadTexts:
    me1200IpmcMvrGroupAddressCountInfoGroup.setStatus("current")

me1200IpmcMvrIgmpVlanStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 7)
)
me1200IpmcMvrIgmpVlanStatusTableInfoGroup.setObjects(
      *(("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusQuerierStatus"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusActiveQuerierAddress"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusQuerierUptime"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusQueryInterval"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusStartupQueryCount"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusQuerierExpiryTime"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusCounterTxQuery"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusCounterTxSpecificQuery"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusCounterRxQuery"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusCounterRxV1Join"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusCounterRxV2Join"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusCounterRxV2Leave"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusCounterRxV3Join"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusCounterRxErrors"))
)
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpVlanStatusTableInfoGroup.setStatus("current")

me1200IpmcMvrIgmpGroupAddressTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 8)
)
me1200IpmcMvrIgmpGroupAddressTableInfoGroup.setObjects(
      *(("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupAddressMemberPorts"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupAddressHardwareSwitch"))
)
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupAddressTableInfoGroup.setStatus("current")

me1200IpmcMvrIgmpGroupSrcListTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 9)
)
me1200IpmcMvrIgmpGroupSrcListTableInfoGroup.setObjects(
      *(("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupSrcListGroupFilterMode"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupSrcListFilterTimer"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupSrcListSourceType"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupSrcListSourceTimer"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupSrcListHardwareFilter"))
)
if mibBuilder.loadTexts:
    me1200IpmcMvrIgmpGroupSrcListTableInfoGroup.setStatus("current")

me1200IpmcMvrMldVlanStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 10)
)
me1200IpmcMvrMldVlanStatusTableInfoGroup.setObjects(
      *(("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusQuerierStatus"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusActiveQuerierAddress"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusQuerierUptime"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusQueryInterval"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusStartupQueryCount"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusQuerierExpiryTime"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusCounterTxQuery"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusCounterTxSpecificQuery"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusCounterRxQuery"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusCounterRxV1Report"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusCounterRxV1Done"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusCounterRxV2Report"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusCounterRxErrors"))
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMldVlanStatusTableInfoGroup.setStatus("current")

me1200IpmcMvrMldGroupAddressTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 11)
)
me1200IpmcMvrMldGroupAddressTableInfoGroup.setObjects(
      *(("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupAddressMemberPorts"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupAddressHardwareSwitch"))
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupAddressTableInfoGroup.setStatus("current")

me1200IpmcMvrMldGroupSrcListTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 12)
)
me1200IpmcMvrMldGroupSrcListTableInfoGroup.setObjects(
      *(("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupSrcListGroupFilterMode"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupSrcListFilterTimer"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupSrcListSourceType"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupSrcListSourceTimer"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupSrcListHardwareFilter"))
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMldGroupSrcListTableInfoGroup.setStatus("current")

me1200IpmcMvrControlStatisticsClearInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 2, 13)
)
me1200IpmcMvrControlStatisticsClearInfoGroup.setObjects(
    ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrControlStatisticsClearIfIndex")
)
if mibBuilder.loadTexts:
    me1200IpmcMvrControlStatisticsClearInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200IpmcMvrMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 68, 2, 1, 1)
)
me1200IpmcMvrMibCompliance.setObjects(
      *(("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrGlobalsInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrPortTableInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrInterfaceTableRowEditorInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrVlanPortTableInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrGroupAddressCountInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpVlanStatusTableInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupAddressTableInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrIgmpGroupSrcListTableInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldVlanStatusTableInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupAddressTableInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrMldGroupSrcListTableInfoGroup"),
        ("ME1200-IPMC-MVR-MIB", "me1200IpmcMvrControlStatisticsClearInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200IpmcMvrMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-IPMC-MVR-MIB",
    **{"ME1200IpmcMvrVlanInterfaceMode": ME1200IpmcMvrVlanInterfaceMode,
       "ME1200IpmcMvrVlanInterfaceTagging": ME1200IpmcMvrVlanInterfaceTagging,
       "ME1200IpmcMvrVlanInterfacePortRole": ME1200IpmcMvrVlanInterfacePortRole,
       "ME1200IpmcMvrInterfaceQuerierStatus": ME1200IpmcMvrInterfaceQuerierStatus,
       "ME1200IpmcMvrGroupSrcListGroupFilterMode": ME1200IpmcMvrGroupSrcListGroupFilterMode,
       "ME1200IpmcMvrGroupSrcListSourceType": ME1200IpmcMvrGroupSrcListSourceType,
       "me1200IpmcMvrMib": me1200IpmcMvrMib,
       "me1200IpmcMvrMIBObjects": me1200IpmcMvrMIBObjects,
       "me1200IpmcMvrConfig": me1200IpmcMvrConfig,
       "me1200IpmcMvrGlobals": me1200IpmcMvrGlobals,
       "me1200IpmcMvrGlobalsAdminState": me1200IpmcMvrGlobalsAdminState,
       "me1200IpmcMvrPortTable": me1200IpmcMvrPortTable,
       "me1200IpmcMvrPortEntry": me1200IpmcMvrPortEntry,
       "me1200IpmcMvrPortPortIndex": me1200IpmcMvrPortPortIndex,
       "me1200IpmcMvrPortDoImmediateLeave": me1200IpmcMvrPortDoImmediateLeave,
       "me1200IpmcMvrInterfaceTable": me1200IpmcMvrInterfaceTable,
       "me1200IpmcMvrInterfaceEntry": me1200IpmcMvrInterfaceEntry,
       "me1200IpmcMvrInterfaceIfIndex": me1200IpmcMvrInterfaceIfIndex,
       "me1200IpmcMvrInterfaceName": me1200IpmcMvrInterfaceName,
       "me1200IpmcMvrInterfaceIgmpQuerierAddress": me1200IpmcMvrInterfaceIgmpQuerierAddress,
       "me1200IpmcMvrInterfaceMode": me1200IpmcMvrInterfaceMode,
       "me1200IpmcMvrInterfaceTagging": me1200IpmcMvrInterfaceTagging,
       "me1200IpmcMvrInterfacePriority": me1200IpmcMvrInterfacePriority,
       "me1200IpmcMvrInterfaceLastListenerQueryInterval": me1200IpmcMvrInterfaceLastListenerQueryInterval,
       "me1200IpmcMvrInterfaceChannelProfile": me1200IpmcMvrInterfaceChannelProfile,
       "me1200IpmcMvrInterfaceAction": me1200IpmcMvrInterfaceAction,
       "me1200IpmcMvrInterfaceTableRowEditor": me1200IpmcMvrInterfaceTableRowEditor,
       "me1200IpmcMvrInterfaceTableRowEditorIfIndex": me1200IpmcMvrInterfaceTableRowEditorIfIndex,
       "me1200IpmcMvrInterfaceTableRowEditorName": me1200IpmcMvrInterfaceTableRowEditorName,
       "me1200IpmcMvrInterfaceTableRowEditorIgmpQuerierAddress": me1200IpmcMvrInterfaceTableRowEditorIgmpQuerierAddress,
       "me1200IpmcMvrInterfaceTableRowEditorMode": me1200IpmcMvrInterfaceTableRowEditorMode,
       "me1200IpmcMvrInterfaceTableRowEditorTagging": me1200IpmcMvrInterfaceTableRowEditorTagging,
       "me1200IpmcMvrInterfaceTableRowEditorPriority": me1200IpmcMvrInterfaceTableRowEditorPriority,
       "me1200IpmcMvrInterfaceTableRowEditorLastListenerQueryInterval": me1200IpmcMvrInterfaceTableRowEditorLastListenerQueryInterval,
       "me1200IpmcMvrInterfaceTableRowEditorChannelProfile": me1200IpmcMvrInterfaceTableRowEditorChannelProfile,
       "me1200IpmcMvrInterfaceTableRowEditorAction": me1200IpmcMvrInterfaceTableRowEditorAction,
       "me1200IpmcMvrVlanPortTable": me1200IpmcMvrVlanPortTable,
       "me1200IpmcMvrVlanPortEntry": me1200IpmcMvrVlanPortEntry,
       "me1200IpmcMvrVlanPortIfIndex": me1200IpmcMvrVlanPortIfIndex,
       "me1200IpmcMvrVlanPortPortIndex": me1200IpmcMvrVlanPortPortIndex,
       "me1200IpmcMvrVlanPortRole": me1200IpmcMvrVlanPortRole,
       "me1200IpmcMvrStatus": me1200IpmcMvrStatus,
       "me1200IpmcMvrGroupAddressCount": me1200IpmcMvrGroupAddressCount,
       "me1200IpmcMvrGroupAddressCountFromIgmp": me1200IpmcMvrGroupAddressCountFromIgmp,
       "me1200IpmcMvrGroupAddressCountFromMld": me1200IpmcMvrGroupAddressCountFromMld,
       "me1200IpmcMvrIgmpVlanStatusTable": me1200IpmcMvrIgmpVlanStatusTable,
       "me1200IpmcMvrIgmpVlanStatusEntry": me1200IpmcMvrIgmpVlanStatusEntry,
       "me1200IpmcMvrIgmpVlanStatusIfIndex": me1200IpmcMvrIgmpVlanStatusIfIndex,
       "me1200IpmcMvrIgmpVlanStatusQuerierStatus": me1200IpmcMvrIgmpVlanStatusQuerierStatus,
       "me1200IpmcMvrIgmpVlanStatusActiveQuerierAddress": me1200IpmcMvrIgmpVlanStatusActiveQuerierAddress,
       "me1200IpmcMvrIgmpVlanStatusQuerierUptime": me1200IpmcMvrIgmpVlanStatusQuerierUptime,
       "me1200IpmcMvrIgmpVlanStatusQueryInterval": me1200IpmcMvrIgmpVlanStatusQueryInterval,
       "me1200IpmcMvrIgmpVlanStatusStartupQueryCount": me1200IpmcMvrIgmpVlanStatusStartupQueryCount,
       "me1200IpmcMvrIgmpVlanStatusQuerierExpiryTime": me1200IpmcMvrIgmpVlanStatusQuerierExpiryTime,
       "me1200IpmcMvrIgmpVlanStatusCounterTxQuery": me1200IpmcMvrIgmpVlanStatusCounterTxQuery,
       "me1200IpmcMvrIgmpVlanStatusCounterTxSpecificQuery": me1200IpmcMvrIgmpVlanStatusCounterTxSpecificQuery,
       "me1200IpmcMvrIgmpVlanStatusCounterRxQuery": me1200IpmcMvrIgmpVlanStatusCounterRxQuery,
       "me1200IpmcMvrIgmpVlanStatusCounterRxV1Join": me1200IpmcMvrIgmpVlanStatusCounterRxV1Join,
       "me1200IpmcMvrIgmpVlanStatusCounterRxV2Join": me1200IpmcMvrIgmpVlanStatusCounterRxV2Join,
       "me1200IpmcMvrIgmpVlanStatusCounterRxV2Leave": me1200IpmcMvrIgmpVlanStatusCounterRxV2Leave,
       "me1200IpmcMvrIgmpVlanStatusCounterRxV3Join": me1200IpmcMvrIgmpVlanStatusCounterRxV3Join,
       "me1200IpmcMvrIgmpVlanStatusCounterRxErrors": me1200IpmcMvrIgmpVlanStatusCounterRxErrors,
       "me1200IpmcMvrIgmpGroupAddressTable": me1200IpmcMvrIgmpGroupAddressTable,
       "me1200IpmcMvrIgmpGroupAddressEntry": me1200IpmcMvrIgmpGroupAddressEntry,
       "me1200IpmcMvrIgmpGroupAddressIfIndex": me1200IpmcMvrIgmpGroupAddressIfIndex,
       "me1200IpmcMvrIgmpGroupAddressGroupAddress": me1200IpmcMvrIgmpGroupAddressGroupAddress,
       "me1200IpmcMvrIgmpGroupAddressMemberPorts": me1200IpmcMvrIgmpGroupAddressMemberPorts,
       "me1200IpmcMvrIgmpGroupAddressHardwareSwitch": me1200IpmcMvrIgmpGroupAddressHardwareSwitch,
       "me1200IpmcMvrIgmpGroupSrcListTable": me1200IpmcMvrIgmpGroupSrcListTable,
       "me1200IpmcMvrIgmpGroupSrcListEntry": me1200IpmcMvrIgmpGroupSrcListEntry,
       "me1200IpmcMvrIgmpGroupSrcListIfIndex": me1200IpmcMvrIgmpGroupSrcListIfIndex,
       "me1200IpmcMvrIgmpGroupSrcListGroupAddress": me1200IpmcMvrIgmpGroupSrcListGroupAddress,
       "me1200IpmcMvrIgmpGroupSrcListPortIndex": me1200IpmcMvrIgmpGroupSrcListPortIndex,
       "me1200IpmcMvrIgmpGroupSrcListHostAddress": me1200IpmcMvrIgmpGroupSrcListHostAddress,
       "me1200IpmcMvrIgmpGroupSrcListGroupFilterMode": me1200IpmcMvrIgmpGroupSrcListGroupFilterMode,
       "me1200IpmcMvrIgmpGroupSrcListFilterTimer": me1200IpmcMvrIgmpGroupSrcListFilterTimer,
       "me1200IpmcMvrIgmpGroupSrcListSourceType": me1200IpmcMvrIgmpGroupSrcListSourceType,
       "me1200IpmcMvrIgmpGroupSrcListSourceTimer": me1200IpmcMvrIgmpGroupSrcListSourceTimer,
       "me1200IpmcMvrIgmpGroupSrcListHardwareFilter": me1200IpmcMvrIgmpGroupSrcListHardwareFilter,
       "me1200IpmcMvrMldVlanStatusTable": me1200IpmcMvrMldVlanStatusTable,
       "me1200IpmcMvrMldVlanStatusEntry": me1200IpmcMvrMldVlanStatusEntry,
       "me1200IpmcMvrMldVlanStatusIfIndex": me1200IpmcMvrMldVlanStatusIfIndex,
       "me1200IpmcMvrMldVlanStatusQuerierStatus": me1200IpmcMvrMldVlanStatusQuerierStatus,
       "me1200IpmcMvrMldVlanStatusActiveQuerierAddress": me1200IpmcMvrMldVlanStatusActiveQuerierAddress,
       "me1200IpmcMvrMldVlanStatusQuerierUptime": me1200IpmcMvrMldVlanStatusQuerierUptime,
       "me1200IpmcMvrMldVlanStatusQueryInterval": me1200IpmcMvrMldVlanStatusQueryInterval,
       "me1200IpmcMvrMldVlanStatusStartupQueryCount": me1200IpmcMvrMldVlanStatusStartupQueryCount,
       "me1200IpmcMvrMldVlanStatusQuerierExpiryTime": me1200IpmcMvrMldVlanStatusQuerierExpiryTime,
       "me1200IpmcMvrMldVlanStatusCounterTxQuery": me1200IpmcMvrMldVlanStatusCounterTxQuery,
       "me1200IpmcMvrMldVlanStatusCounterTxSpecificQuery": me1200IpmcMvrMldVlanStatusCounterTxSpecificQuery,
       "me1200IpmcMvrMldVlanStatusCounterRxQuery": me1200IpmcMvrMldVlanStatusCounterRxQuery,
       "me1200IpmcMvrMldVlanStatusCounterRxV1Report": me1200IpmcMvrMldVlanStatusCounterRxV1Report,
       "me1200IpmcMvrMldVlanStatusCounterRxV1Done": me1200IpmcMvrMldVlanStatusCounterRxV1Done,
       "me1200IpmcMvrMldVlanStatusCounterRxV2Report": me1200IpmcMvrMldVlanStatusCounterRxV2Report,
       "me1200IpmcMvrMldVlanStatusCounterRxErrors": me1200IpmcMvrMldVlanStatusCounterRxErrors,
       "me1200IpmcMvrMldGroupAddressTable": me1200IpmcMvrMldGroupAddressTable,
       "me1200IpmcMvrMldGroupAddressEntry": me1200IpmcMvrMldGroupAddressEntry,
       "me1200IpmcMvrMldGroupAddressIfIndex": me1200IpmcMvrMldGroupAddressIfIndex,
       "me1200IpmcMvrMldGroupAddressGroupAddress": me1200IpmcMvrMldGroupAddressGroupAddress,
       "me1200IpmcMvrMldGroupAddressMemberPorts": me1200IpmcMvrMldGroupAddressMemberPorts,
       "me1200IpmcMvrMldGroupAddressHardwareSwitch": me1200IpmcMvrMldGroupAddressHardwareSwitch,
       "me1200IpmcMvrMldGroupSrcListTable": me1200IpmcMvrMldGroupSrcListTable,
       "me1200IpmcMvrMldGroupSrcListEntry": me1200IpmcMvrMldGroupSrcListEntry,
       "me1200IpmcMvrMldGroupSrcListIfIndex": me1200IpmcMvrMldGroupSrcListIfIndex,
       "me1200IpmcMvrMldGroupSrcListGroupAddress": me1200IpmcMvrMldGroupSrcListGroupAddress,
       "me1200IpmcMvrMldGroupSrcListPortIndex": me1200IpmcMvrMldGroupSrcListPortIndex,
       "me1200IpmcMvrMldGroupSrcListHostAddress": me1200IpmcMvrMldGroupSrcListHostAddress,
       "me1200IpmcMvrMldGroupSrcListGroupFilterMode": me1200IpmcMvrMldGroupSrcListGroupFilterMode,
       "me1200IpmcMvrMldGroupSrcListFilterTimer": me1200IpmcMvrMldGroupSrcListFilterTimer,
       "me1200IpmcMvrMldGroupSrcListSourceType": me1200IpmcMvrMldGroupSrcListSourceType,
       "me1200IpmcMvrMldGroupSrcListSourceTimer": me1200IpmcMvrMldGroupSrcListSourceTimer,
       "me1200IpmcMvrMldGroupSrcListHardwareFilter": me1200IpmcMvrMldGroupSrcListHardwareFilter,
       "me1200IpmcMvrControl": me1200IpmcMvrControl,
       "me1200IpmcMvrControlStatisticsClear": me1200IpmcMvrControlStatisticsClear,
       "me1200IpmcMvrControlStatisticsClearIfIndex": me1200IpmcMvrControlStatisticsClearIfIndex,
       "me1200IpmcMvrMIBConformance": me1200IpmcMvrMIBConformance,
       "me1200IpmcMvrMIBCompliances": me1200IpmcMvrMIBCompliances,
       "me1200IpmcMvrMibCompliance": me1200IpmcMvrMibCompliance,
       "me1200IpmcMvrMIBGroups": me1200IpmcMvrMIBGroups,
       "me1200IpmcMvrGlobalsInfoGroup": me1200IpmcMvrGlobalsInfoGroup,
       "me1200IpmcMvrPortTableInfoGroup": me1200IpmcMvrPortTableInfoGroup,
       "me1200IpmcMvrInterfaceTableInfoGroup": me1200IpmcMvrInterfaceTableInfoGroup,
       "me1200IpmcMvrInterfaceTableRowEditorInfoGroup": me1200IpmcMvrInterfaceTableRowEditorInfoGroup,
       "me1200IpmcMvrVlanPortTableInfoGroup": me1200IpmcMvrVlanPortTableInfoGroup,
       "me1200IpmcMvrGroupAddressCountInfoGroup": me1200IpmcMvrGroupAddressCountInfoGroup,
       "me1200IpmcMvrIgmpVlanStatusTableInfoGroup": me1200IpmcMvrIgmpVlanStatusTableInfoGroup,
       "me1200IpmcMvrIgmpGroupAddressTableInfoGroup": me1200IpmcMvrIgmpGroupAddressTableInfoGroup,
       "me1200IpmcMvrIgmpGroupSrcListTableInfoGroup": me1200IpmcMvrIgmpGroupSrcListTableInfoGroup,
       "me1200IpmcMvrMldVlanStatusTableInfoGroup": me1200IpmcMvrMldVlanStatusTableInfoGroup,
       "me1200IpmcMvrMldGroupAddressTableInfoGroup": me1200IpmcMvrMldGroupAddressTableInfoGroup,
       "me1200IpmcMvrMldGroupSrcListTableInfoGroup": me1200IpmcMvrMldGroupSrcListTableInfoGroup,
       "me1200IpmcMvrControlStatisticsClearInfoGroup": me1200IpmcMvrControlStatisticsClearInfoGroup}
)
