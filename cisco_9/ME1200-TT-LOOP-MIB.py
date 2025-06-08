# SNMP MIB module (ME1200-TT-LOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-TT-LOOP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(ME1200DisplayString,
 ME1200InterfaceIndex,
 ME1200RowEditorState) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex",
    "ME1200RowEditorState")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

me1200TtLoopMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128)
)
if mibBuilder.loadTexts:
    me1200TtLoopMib.setRevisions(
        ("2014-05-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200TtLoopInstanceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("macLoop", 0),
          ("oamLoop", 1))
    )



class ME1200TtLoopInstanceDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("facility", 0),
          ("terminal", 1))
    )



class ME1200TtLoopInstanceDomain(TextualConvention, Integer32):
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
        *(("port", 0),
          ("evc", 1),
          ("vlan", 2))
    )



class ME1200TtLoopInstanceSubscriber(TextualConvention, Integer32):
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
        *(("none", 0),
          ("all", 1),
          ("test", 2))
    )



class ME1200TtLoopInstanceAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("adminDisabled", 0),
          ("adminEnabled", 1))
    )



class ME1200TtLoopInstanceOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("operDown", 0),
          ("operUp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200TtLoopMibObjects_ObjectIdentity = ObjectIdentity
me1200TtLoopMibObjects = _Me1200TtLoopMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1)
)
_Me1200TtLoopCapabilities_ObjectIdentity = ObjectIdentity
me1200TtLoopCapabilities = _Me1200TtLoopCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 1)
)
_Me1200TtLoopCapabilitiesInstanceMax_Type = Unsigned32
_Me1200TtLoopCapabilitiesInstanceMax_Object = MibScalar
me1200TtLoopCapabilitiesInstanceMax = _Me1200TtLoopCapabilitiesInstanceMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 1, 1),
    _Me1200TtLoopCapabilitiesInstanceMax_Type()
)
me1200TtLoopCapabilitiesInstanceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200TtLoopCapabilitiesInstanceMax.setStatus("current")
_Me1200TtLoopCapabilitiesNameMax_Type = Unsigned32
_Me1200TtLoopCapabilitiesNameMax_Object = MibScalar
me1200TtLoopCapabilitiesNameMax = _Me1200TtLoopCapabilitiesNameMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 1, 2),
    _Me1200TtLoopCapabilitiesNameMax_Type()
)
me1200TtLoopCapabilitiesNameMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200TtLoopCapabilitiesNameMax.setStatus("current")
_Me1200TtLoopConfig_ObjectIdentity = ObjectIdentity
me1200TtLoopConfig = _Me1200TtLoopConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2)
)
_Me1200TtLoopConfigInstanceTable_Object = MibTable
me1200TtLoopConfigInstanceTable = _Me1200TtLoopConfigInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1)
)
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceTable.setStatus("current")
_Me1200TtLoopConfigInstanceEntry_Object = MibTableRow
me1200TtLoopConfigInstanceEntry = _Me1200TtLoopConfigInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1)
)
me1200TtLoopConfigInstanceEntry.setIndexNames(
    (0, "ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceId"),
)
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceEntry.setStatus("current")


class _Me1200TtLoopConfigInstanceId_Type(Integer32):
    """Custom type me1200TtLoopConfigInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200TtLoopConfigInstanceId_Type.__name__ = "Integer32"
_Me1200TtLoopConfigInstanceId_Object = MibTableColumn
me1200TtLoopConfigInstanceId = _Me1200TtLoopConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 1),
    _Me1200TtLoopConfigInstanceId_Type()
)
me1200TtLoopConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceId.setStatus("current")


class _Me1200TtLoopConfigInstanceName_Type(ME1200DisplayString):
    """Custom type me1200TtLoopConfigInstanceName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200TtLoopConfigInstanceName_Type.__name__ = "ME1200DisplayString"
_Me1200TtLoopConfigInstanceName_Object = MibTableColumn
me1200TtLoopConfigInstanceName = _Me1200TtLoopConfigInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 2),
    _Me1200TtLoopConfigInstanceName_Type()
)
me1200TtLoopConfigInstanceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceName.setStatus("current")
_Me1200TtLoopConfigInstanceType_Type = ME1200TtLoopInstanceType
_Me1200TtLoopConfigInstanceType_Object = MibTableColumn
me1200TtLoopConfigInstanceType = _Me1200TtLoopConfigInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 3),
    _Me1200TtLoopConfigInstanceType_Type()
)
me1200TtLoopConfigInstanceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceType.setStatus("current")
_Me1200TtLoopConfigInstanceDirection_Type = ME1200TtLoopInstanceDirection
_Me1200TtLoopConfigInstanceDirection_Object = MibTableColumn
me1200TtLoopConfigInstanceDirection = _Me1200TtLoopConfigInstanceDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 4),
    _Me1200TtLoopConfigInstanceDirection_Type()
)
me1200TtLoopConfigInstanceDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceDirection.setStatus("current")
_Me1200TtLoopConfigInstanceDomain_Type = ME1200TtLoopInstanceDomain
_Me1200TtLoopConfigInstanceDomain_Object = MibTableColumn
me1200TtLoopConfigInstanceDomain = _Me1200TtLoopConfigInstanceDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 5),
    _Me1200TtLoopConfigInstanceDomain_Type()
)
me1200TtLoopConfigInstanceDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceDomain.setStatus("current")
_Me1200TtLoopConfigInstanceFlow_Type = Unsigned32
_Me1200TtLoopConfigInstanceFlow_Object = MibTableColumn
me1200TtLoopConfigInstanceFlow = _Me1200TtLoopConfigInstanceFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 6),
    _Me1200TtLoopConfigInstanceFlow_Type()
)
me1200TtLoopConfigInstanceFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceFlow.setStatus("current")
_Me1200TtLoopConfigInstancePort_Type = ME1200InterfaceIndex
_Me1200TtLoopConfigInstancePort_Object = MibTableColumn
me1200TtLoopConfigInstancePort = _Me1200TtLoopConfigInstancePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 7),
    _Me1200TtLoopConfigInstancePort_Type()
)
me1200TtLoopConfigInstancePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstancePort.setStatus("current")
_Me1200TtLoopConfigInstanceLevel_Type = Unsigned32
_Me1200TtLoopConfigInstanceLevel_Object = MibTableColumn
me1200TtLoopConfigInstanceLevel = _Me1200TtLoopConfigInstanceLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 8),
    _Me1200TtLoopConfigInstanceLevel_Type()
)
me1200TtLoopConfigInstanceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceLevel.setStatus("current")
_Me1200TtLoopConfigInstanceSubscriber_Type = ME1200TtLoopInstanceSubscriber
_Me1200TtLoopConfigInstanceSubscriber_Object = MibTableColumn
me1200TtLoopConfigInstanceSubscriber = _Me1200TtLoopConfigInstanceSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 9),
    _Me1200TtLoopConfigInstanceSubscriber_Type()
)
me1200TtLoopConfigInstanceSubscriber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceSubscriber.setStatus("current")
_Me1200TtLoopConfigInstanceAdminState_Type = ME1200TtLoopInstanceAdminState
_Me1200TtLoopConfigInstanceAdminState_Object = MibTableColumn
me1200TtLoopConfigInstanceAdminState = _Me1200TtLoopConfigInstanceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 10),
    _Me1200TtLoopConfigInstanceAdminState_Type()
)
me1200TtLoopConfigInstanceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceAdminState.setStatus("current")
_Me1200TtLoopConfigInstanceAction_Type = ME1200RowEditorState
_Me1200TtLoopConfigInstanceAction_Object = MibTableColumn
me1200TtLoopConfigInstanceAction = _Me1200TtLoopConfigInstanceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 1, 1, 100),
    _Me1200TtLoopConfigInstanceAction_Type()
)
me1200TtLoopConfigInstanceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceAction.setStatus("current")
_Me1200TtLoopConfigInstanceRowEditor_ObjectIdentity = ObjectIdentity
me1200TtLoopConfigInstanceRowEditor = _Me1200TtLoopConfigInstanceRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2)
)


class _Me1200TtLoopConfigInstanceRowEditorId_Type(Integer32):
    """Custom type me1200TtLoopConfigInstanceRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200TtLoopConfigInstanceRowEditorId_Type.__name__ = "Integer32"
_Me1200TtLoopConfigInstanceRowEditorId_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorId = _Me1200TtLoopConfigInstanceRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 1),
    _Me1200TtLoopConfigInstanceRowEditorId_Type()
)
me1200TtLoopConfigInstanceRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorId.setStatus("current")


class _Me1200TtLoopConfigInstanceRowEditorName_Type(ME1200DisplayString):
    """Custom type me1200TtLoopConfigInstanceRowEditorName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200TtLoopConfigInstanceRowEditorName_Type.__name__ = "ME1200DisplayString"
_Me1200TtLoopConfigInstanceRowEditorName_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorName = _Me1200TtLoopConfigInstanceRowEditorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 2),
    _Me1200TtLoopConfigInstanceRowEditorName_Type()
)
me1200TtLoopConfigInstanceRowEditorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorName.setStatus("current")
_Me1200TtLoopConfigInstanceRowEditorType_Type = ME1200TtLoopInstanceType
_Me1200TtLoopConfigInstanceRowEditorType_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorType = _Me1200TtLoopConfigInstanceRowEditorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 3),
    _Me1200TtLoopConfigInstanceRowEditorType_Type()
)
me1200TtLoopConfigInstanceRowEditorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorType.setStatus("current")
_Me1200TtLoopConfigInstanceRowEditorDirection_Type = ME1200TtLoopInstanceDirection
_Me1200TtLoopConfigInstanceRowEditorDirection_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorDirection = _Me1200TtLoopConfigInstanceRowEditorDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 4),
    _Me1200TtLoopConfigInstanceRowEditorDirection_Type()
)
me1200TtLoopConfigInstanceRowEditorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorDirection.setStatus("current")
_Me1200TtLoopConfigInstanceRowEditorDomain_Type = ME1200TtLoopInstanceDomain
_Me1200TtLoopConfigInstanceRowEditorDomain_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorDomain = _Me1200TtLoopConfigInstanceRowEditorDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 5),
    _Me1200TtLoopConfigInstanceRowEditorDomain_Type()
)
me1200TtLoopConfigInstanceRowEditorDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorDomain.setStatus("current")
_Me1200TtLoopConfigInstanceRowEditorFlow_Type = Unsigned32
_Me1200TtLoopConfigInstanceRowEditorFlow_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorFlow = _Me1200TtLoopConfigInstanceRowEditorFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 6),
    _Me1200TtLoopConfigInstanceRowEditorFlow_Type()
)
me1200TtLoopConfigInstanceRowEditorFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorFlow.setStatus("current")
_Me1200TtLoopConfigInstanceRowEditorPort_Type = ME1200InterfaceIndex
_Me1200TtLoopConfigInstanceRowEditorPort_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorPort = _Me1200TtLoopConfigInstanceRowEditorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 7),
    _Me1200TtLoopConfigInstanceRowEditorPort_Type()
)
me1200TtLoopConfigInstanceRowEditorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorPort.setStatus("current")
_Me1200TtLoopConfigInstanceRowEditorLevel_Type = Unsigned32
_Me1200TtLoopConfigInstanceRowEditorLevel_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorLevel = _Me1200TtLoopConfigInstanceRowEditorLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 8),
    _Me1200TtLoopConfigInstanceRowEditorLevel_Type()
)
me1200TtLoopConfigInstanceRowEditorLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorLevel.setStatus("current")
_Me1200TtLoopConfigInstanceRowEditorSubscriber_Type = ME1200TtLoopInstanceSubscriber
_Me1200TtLoopConfigInstanceRowEditorSubscriber_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorSubscriber = _Me1200TtLoopConfigInstanceRowEditorSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 9),
    _Me1200TtLoopConfigInstanceRowEditorSubscriber_Type()
)
me1200TtLoopConfigInstanceRowEditorSubscriber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorSubscriber.setStatus("current")
_Me1200TtLoopConfigInstanceRowEditorAdminState_Type = ME1200TtLoopInstanceAdminState
_Me1200TtLoopConfigInstanceRowEditorAdminState_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorAdminState = _Me1200TtLoopConfigInstanceRowEditorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 10),
    _Me1200TtLoopConfigInstanceRowEditorAdminState_Type()
)
me1200TtLoopConfigInstanceRowEditorAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorAdminState.setStatus("current")
_Me1200TtLoopConfigInstanceRowEditorAction_Type = ME1200RowEditorState
_Me1200TtLoopConfigInstanceRowEditorAction_Object = MibScalar
me1200TtLoopConfigInstanceRowEditorAction = _Me1200TtLoopConfigInstanceRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 2, 2, 100),
    _Me1200TtLoopConfigInstanceRowEditorAction_Type()
)
me1200TtLoopConfigInstanceRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorAction.setStatus("current")
_Me1200TtLoopStatus_ObjectIdentity = ObjectIdentity
me1200TtLoopStatus = _Me1200TtLoopStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3)
)
_Me1200TtLoopStatusInstanceTable_Object = MibTable
me1200TtLoopStatusInstanceTable = _Me1200TtLoopStatusInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200TtLoopStatusInstanceTable.setStatus("current")
_Me1200TtLoopStatusInstanceEntry_Object = MibTableRow
me1200TtLoopStatusInstanceEntry = _Me1200TtLoopStatusInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 1, 1)
)
me1200TtLoopStatusInstanceEntry.setIndexNames(
    (0, "ME1200-TT-LOOP-MIB", "me1200TtLoopStatusInstanceId"),
)
if mibBuilder.loadTexts:
    me1200TtLoopStatusInstanceEntry.setStatus("current")


class _Me1200TtLoopStatusInstanceId_Type(Integer32):
    """Custom type me1200TtLoopStatusInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200TtLoopStatusInstanceId_Type.__name__ = "Integer32"
_Me1200TtLoopStatusInstanceId_Object = MibTableColumn
me1200TtLoopStatusInstanceId = _Me1200TtLoopStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 1, 1, 1),
    _Me1200TtLoopStatusInstanceId_Type()
)
me1200TtLoopStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200TtLoopStatusInstanceId.setStatus("current")
_Me1200TtLoopStatusInstanceOperState_Type = ME1200TtLoopInstanceOperState
_Me1200TtLoopStatusInstanceOperState_Object = MibTableColumn
me1200TtLoopStatusInstanceOperState = _Me1200TtLoopStatusInstanceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 1, 3, 1, 1, 2),
    _Me1200TtLoopStatusInstanceOperState_Type()
)
me1200TtLoopStatusInstanceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200TtLoopStatusInstanceOperState.setStatus("current")
_Me1200TtLoopMibConformance_ObjectIdentity = ObjectIdentity
me1200TtLoopMibConformance = _Me1200TtLoopMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3)
)
_Me1200TtLoopMibCompliances_ObjectIdentity = ObjectIdentity
me1200TtLoopMibCompliances = _Me1200TtLoopMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 1)
)
_Me1200TtLoopMibGroups_ObjectIdentity = ObjectIdentity
me1200TtLoopMibGroups = _Me1200TtLoopMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2)
)

# Managed Objects groups

me1200TtLoopCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2, 1)
)
me1200TtLoopCapabilitiesInfoGroup.setObjects(
      *(("ME1200-TT-LOOP-MIB", "me1200TtLoopCapabilitiesInstanceMax"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopCapabilitiesNameMax"))
)
if mibBuilder.loadTexts:
    me1200TtLoopCapabilitiesInfoGroup.setStatus("current")

me1200TtLoopConfigInstanceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2, 2)
)
me1200TtLoopConfigInstanceTableInfoGroup.setObjects(
      *(("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceName"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceType"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceDirection"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceDomain"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceFlow"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstancePort"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceLevel"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceSubscriber"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceAdminState"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceAction"))
)
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceTableInfoGroup.setStatus("current")

me1200TtLoopConfigInstanceRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2, 3)
)
me1200TtLoopConfigInstanceRowEditorInfoGroup.setObjects(
      *(("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorId"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorName"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorType"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorDirection"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorDomain"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorFlow"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorPort"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorLevel"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorSubscriber"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorAdminState"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200TtLoopConfigInstanceRowEditorInfoGroup.setStatus("current")

me1200TtLoopStatusInstanceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 2, 4)
)
me1200TtLoopStatusInstanceTableInfoGroup.setObjects(
    ("ME1200-TT-LOOP-MIB", "me1200TtLoopStatusInstanceOperState")
)
if mibBuilder.loadTexts:
    me1200TtLoopStatusInstanceTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200TtLoopMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 128, 3, 1, 1)
)
me1200TtLoopMibCompliance.setObjects(
      *(("ME1200-TT-LOOP-MIB", "me1200TtLoopCapabilitiesInfoGroup"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceTableInfoGroup"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopConfigInstanceRowEditorInfoGroup"),
        ("ME1200-TT-LOOP-MIB", "me1200TtLoopStatusInstanceTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200TtLoopMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-TT-LOOP-MIB",
    **{"ME1200TtLoopInstanceType": ME1200TtLoopInstanceType,
       "ME1200TtLoopInstanceDirection": ME1200TtLoopInstanceDirection,
       "ME1200TtLoopInstanceDomain": ME1200TtLoopInstanceDomain,
       "ME1200TtLoopInstanceSubscriber": ME1200TtLoopInstanceSubscriber,
       "ME1200TtLoopInstanceAdminState": ME1200TtLoopInstanceAdminState,
       "ME1200TtLoopInstanceOperState": ME1200TtLoopInstanceOperState,
       "me1200TtLoopMib": me1200TtLoopMib,
       "me1200TtLoopMibObjects": me1200TtLoopMibObjects,
       "me1200TtLoopCapabilities": me1200TtLoopCapabilities,
       "me1200TtLoopCapabilitiesInstanceMax": me1200TtLoopCapabilitiesInstanceMax,
       "me1200TtLoopCapabilitiesNameMax": me1200TtLoopCapabilitiesNameMax,
       "me1200TtLoopConfig": me1200TtLoopConfig,
       "me1200TtLoopConfigInstanceTable": me1200TtLoopConfigInstanceTable,
       "me1200TtLoopConfigInstanceEntry": me1200TtLoopConfigInstanceEntry,
       "me1200TtLoopConfigInstanceId": me1200TtLoopConfigInstanceId,
       "me1200TtLoopConfigInstanceName": me1200TtLoopConfigInstanceName,
       "me1200TtLoopConfigInstanceType": me1200TtLoopConfigInstanceType,
       "me1200TtLoopConfigInstanceDirection": me1200TtLoopConfigInstanceDirection,
       "me1200TtLoopConfigInstanceDomain": me1200TtLoopConfigInstanceDomain,
       "me1200TtLoopConfigInstanceFlow": me1200TtLoopConfigInstanceFlow,
       "me1200TtLoopConfigInstancePort": me1200TtLoopConfigInstancePort,
       "me1200TtLoopConfigInstanceLevel": me1200TtLoopConfigInstanceLevel,
       "me1200TtLoopConfigInstanceSubscriber": me1200TtLoopConfigInstanceSubscriber,
       "me1200TtLoopConfigInstanceAdminState": me1200TtLoopConfigInstanceAdminState,
       "me1200TtLoopConfigInstanceAction": me1200TtLoopConfigInstanceAction,
       "me1200TtLoopConfigInstanceRowEditor": me1200TtLoopConfigInstanceRowEditor,
       "me1200TtLoopConfigInstanceRowEditorId": me1200TtLoopConfigInstanceRowEditorId,
       "me1200TtLoopConfigInstanceRowEditorName": me1200TtLoopConfigInstanceRowEditorName,
       "me1200TtLoopConfigInstanceRowEditorType": me1200TtLoopConfigInstanceRowEditorType,
       "me1200TtLoopConfigInstanceRowEditorDirection": me1200TtLoopConfigInstanceRowEditorDirection,
       "me1200TtLoopConfigInstanceRowEditorDomain": me1200TtLoopConfigInstanceRowEditorDomain,
       "me1200TtLoopConfigInstanceRowEditorFlow": me1200TtLoopConfigInstanceRowEditorFlow,
       "me1200TtLoopConfigInstanceRowEditorPort": me1200TtLoopConfigInstanceRowEditorPort,
       "me1200TtLoopConfigInstanceRowEditorLevel": me1200TtLoopConfigInstanceRowEditorLevel,
       "me1200TtLoopConfigInstanceRowEditorSubscriber": me1200TtLoopConfigInstanceRowEditorSubscriber,
       "me1200TtLoopConfigInstanceRowEditorAdminState": me1200TtLoopConfigInstanceRowEditorAdminState,
       "me1200TtLoopConfigInstanceRowEditorAction": me1200TtLoopConfigInstanceRowEditorAction,
       "me1200TtLoopStatus": me1200TtLoopStatus,
       "me1200TtLoopStatusInstanceTable": me1200TtLoopStatusInstanceTable,
       "me1200TtLoopStatusInstanceEntry": me1200TtLoopStatusInstanceEntry,
       "me1200TtLoopStatusInstanceId": me1200TtLoopStatusInstanceId,
       "me1200TtLoopStatusInstanceOperState": me1200TtLoopStatusInstanceOperState,
       "me1200TtLoopMibConformance": me1200TtLoopMibConformance,
       "me1200TtLoopMibCompliances": me1200TtLoopMibCompliances,
       "me1200TtLoopMibCompliance": me1200TtLoopMibCompliance,
       "me1200TtLoopMibGroups": me1200TtLoopMibGroups,
       "me1200TtLoopCapabilitiesInfoGroup": me1200TtLoopCapabilitiesInfoGroup,
       "me1200TtLoopConfigInstanceTableInfoGroup": me1200TtLoopConfigInstanceTableInfoGroup,
       "me1200TtLoopConfigInstanceRowEditorInfoGroup": me1200TtLoopConfigInstanceRowEditorInfoGroup,
       "me1200TtLoopStatusInstanceTableInfoGroup": me1200TtLoopStatusInstanceTableInfoGroup}
)
